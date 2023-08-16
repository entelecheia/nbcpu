import logging
from pathlib import Path
from typing import Dict, List, Optional, Union

import matplotlib.pyplot as plt
import pandas as pd
from hyfi import HyFI
from hyfi.composer import BaseModel

logger = logging.getLogger(__name__)


class TopicAnalysis(BaseModel):
    """
    TopicAnalysis class for analyzing topics related to uncertainty.

    Attributes:
        metadata_file (str): Path to the metadata file.
        data_files (Union[List[str], str]): Path(s) to the topic data file(s).
        meta_columns (Union[List[str], Dict[str, str]]): Columns to select from metadata, with optional renaming.
        data_columns (Union[List[str], Dict[str, str]]): Columns to select from topic data, with optional renaming.
        id_col (str): Identifier column name. Default is "id".
        timestamp_col (str): Timestamp column name. Default is "timestamp".
        text_col (str): Text column name. Default is "text".
        _data_ (Optional[pd.DataFrame]): Internal data storage.
    """

    name: str = "TopicAnalysis"
    metadata_file: str
    data_files: Union[List[str], str]
    meta_columns: Optional[Union[List[str], Dict[str, str]]] = None
    data_columns: Optional[Union[List[str], Dict[str, str]]] = None
    id_col: str = "id"
    timestamp_col: str = "timestamp"
    text_col: str = "text"
    frequency: str = "M"
    rolling_window: int = 3
    output_dir: Union[str, Path] = "workspace/outputs"
    verbose: bool = False

    _data_: Optional[pd.DataFrame] = None
    _metadata_: Optional[pd.DataFrame] = None

    @property
    def data(self) -> pd.DataFrame:
        """Merge three dataframes and return the result."""
        # Implement logic to merge meta_data_file, topic_data_file, and uncertainty_data_file
        # based on the selected columns and renaming if necessary.
        data_files = (
            self.data_files if isinstance(self.data_files, list) else [self.data_files]
        )
        if self._data_ is None:
            data = None
            for data_file in data_files:
                data_ = self.load_data(data_file, self.data_columns)
                data = data_ if data is None else data.merge(data_, on=self.id_col)
            if self.id_col in data.columns:
                data = self.metadata[[self.id_col, self.timestamp_col]].merge(
                    data, on=self.id_col
                )
            self._data_ = data
        return self._data_

    def load_data(
        self,
        data_file: str,
        columns: Optional[Union[List[str], Dict[str, str]]] = None,
    ) -> pd.DataFrame:
        """Load data from the three files."""
        data = HyFI.load_dataframe(data_file, verbose=self.verbose)
        if isinstance(columns, list):
            cols = [col for col in columns if col in data.columns]
            data = data[cols]
        elif isinstance(columns, dict):
            cols = {old: new for old, new in columns.items() if old in data.columns}
            data = data[cols.keys()]
            data.rename(columns=cols, inplace=True)
        # make datatype of id col as string
        if self.id_col in data.columns:
            data[self.id_col] = data[self.id_col].astype(str)
            # remove duplicates
            data.drop_duplicates(subset=[self.id_col], inplace=True)
        return data

    def save_data(self, data: pd.DataFrame, output_file: str) -> None:
        """Save data to a file."""
        if not Path(output_file).is_absolute():
            output_file = Path(self.output_dir) / output_file
        HyFI.save_dataframes(data, output_file, verbose=self.verbose)

    @property
    def metadata(self) -> pd.DataFrame:
        """Return metadata."""
        if self._metadata_ is None:
            self._metadata_ = self.load_data(self.metadata_file, self.meta_columns)
        return self._metadata_

    @property
    def id_timestamp(self) -> pd.DataFrame:
        """Return id and timestamp."""
        return self.metadata[[self.id_col, self.timestamp_col]]

    def eda_metadata(self) -> pd.DataFrame:
        """
        Perform exploratory data analysis on the metadata.

        Returns:
            pd.DataFrame: DataFrame containing EDA results.
        """
        # Retrieve metadata
        meta_data = self.metadata

        # Calculate total number of articles
        total_articles = len(meta_data)

        # Calculate average length of articles
        avg_length = meta_data[self.text_col].apply(len).mean()

        # Yearly statistics of the number of articles and average length
        meta_data["year"] = meta_data[self.timestamp_col].dt.year
        yearly_stats = meta_data.groupby("year").agg(
            num_articles=pd.NamedAgg(column=self.id_col, aggfunc="count"),
            avg_length=pd.NamedAgg(
                column=self.text_col, aggfunc=lambda x: x.apply(len).mean()
            ),
        )
        yearly_stats.reset_index(inplace=True)
        yearly_stats.rename(columns={"year": "Year"}, inplace=True)
        yearly_stats["Year"] = yearly_stats["Year"].astype(str)

        # Append total number of articles and average length to yearly statistics
        yearly_stats = pd.concat(
            [
                yearly_stats,
                pd.DataFrame(
                    {
                        "Year": ["Total"],
                        "num_articles": [total_articles],
                        "avg_length": [avg_length],
                    }
                ),
            ]
        )
        return yearly_stats

    def aggregate(
        self,
        data: Optional[pd.DataFrame] = None,
        frequency: Optional[str] = "M",
        agg_func: Optional[str] = "mean",
    ) -> pd.DataFrame:
        """Aggregate data by a given frequency.

        Args:
            frequency (str): Frequency for aggregation (e.g., 'D' for daily, 'M' for monthly).
            agg_func (str): Aggregation function (e.g., 'mean', 'sum', 'count').

        Returns:
            pd.DataFrame: Aggregated data.
        """
        data = data if data is not None else self.data
        if self.timestamp_col not in data.columns:
            raise ValueError(f"{self.timestamp_col} not in data columns.")
        if agg_func == "count":
            return (
                data.set_index(self.timestamp_col)
                .groupby(pd.Grouper(freq=frequency))
                .count()
            )
        if self.id_col in data.columns:
            data = data.drop(columns=[self.id_col])
        return (
            data.set_index(self.timestamp_col)
            .groupby(pd.Grouper(freq=frequency))
            .agg(agg_func)
        )

    def rolling_average(
        self,
        data: pd.DataFrame,
        rolling_window: Optional[int] = 3,
    ) -> pd.DataFrame:
        """Calculate rolling average with a given window size.

        Args:
            data (pd.DataFrame): Data to apply rolling average.
            window (int): Window size for rolling average. Default is 3.

        Returns:
            pd.DataFrame: Data with rolling average applied.
        """
        return data.rolling(rolling_window).mean()

    def plot(
        self,
        data: pd.DataFrame,
        columns: Optional[List[str]] = None,
        rolling_window: Optional[int] = 3,
        plot_type: Optional[str] = "line",
        output_file: Optional[str] = None,
        title: Optional[str] = None,
        xlabel: Optional[str] = "Date",
        ylabel: Optional[str] = None,
        xtick_every: Optional[int] = None,
        figsize=(20, 10),
    ) -> None:
        """Plot selected columns with rolling average.

        Args:
            data (pd.DataFrame): Data to plot.
            columns (List[str]): Columns to plot.
            rolling_window (int): Window size for rolling average. Default is 3.
            plot_type (str): Plot type (e.g., 'line', 'area', 'bar'). Default is 'line'.
            title (str): Plot title.
            xlabel (str): X-axis label.
            ylabel (str): Y-axis label.
            xtick_every (int): Show xticks every n months.
        """
        data = self.rolling_average(data, rolling_window)
        columns = columns or data.columns
        if plot_type == "line":
            data.plot(y=columns, figsize=figsize)
        elif plot_type == "area":
            data.plot.area(y=columns, figsize=figsize)
        elif plot_type == "bar":
            data.plot.bar(y=columns, figsize=figsize)
        title = title or self.name
        plt.title(title)
        xlabel = xlabel or self.timestamp_col
        plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if xtick_every:
            xticks = data.index.strftime("%Y-%m").tolist()
            # every n months
            xticks = [
                xticks[i] if i % xtick_every == 0 else "" for i in range(len(xticks))
            ]
            plt.xticks(range(len(xticks)), xticks)
        output_filename = f"{title}_{plot_type}_{rolling_window}.png".replace(" ", "_")
        output_file = output_file or Path(self.output_dir) / output_filename
        output_file.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_file)
        plt.show()

    def find_articles(
        self,
        topic: str,
        start_date: str,
        end_date: Optional[str] = None,
        n: int = 10,
        columns: Optional[List[str]] = None,
    ) -> pd.DataFrame:
        """Find articles with the highest topic weight for a given period.

        Args:
            topic (str): Topic to search for.
            start_date (str): Start date of the period.
            end_date (Optional[str]): End date of the period. Default is None.
            n (int): Number of articles to retrieve. Default is 10.

        Returns:
            pd.DataFrame: Articles with the highest topic weight.
        """
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date) if end_date else start_date
        data = self.data[
            (self.data[self.timestamp_col] >= start_date)
            & (self.data[self.timestamp_col] <= end_date)
        ]
        data = self.metadata[[self.id_col, self.text_col]].merge(data, on=self.id_col)
        columns = columns or [self.timestamp_col, self.text_col, topic]
        return data.sort_values(topic, ascending=False)[columns].head(n)
