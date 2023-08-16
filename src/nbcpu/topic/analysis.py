from typing import Dict, List, Optional, Union

import matplotlib.pyplot as plt
import pandas as pd
from hyfi import HyFI
from hyfi.composer import BaseModel


class TopicAnalysis(BaseModel):
    """
    TopicAnalysis class for analyzing topics related to uncertainty.

    Attributes:
        meta_data_file (str): Path to the metadata file.
        topic_data_file (str): Path to the topic data file.
        uncertainty_data_file (str): Path to the uncertainty data file.
        meta_columns (Union[List[str], Dict[str, str]]): Columns to select from metadata, with optional renaming.
        topic_columns (Union[List[str], Dict[str, str]]): Columns to select from topic data, with optional renaming.
        uncertainty_columns (Union[List[str], Dict[str, str]]): Columns to select from uncertainty data, with optional renaming.
        id_col (str): Identifier column name. Default is "id".
        timestamp_col (str): Timestamp column name. Default is "timestamp".
        text_col (str): Text column name. Default is "text".
        _data_ (Optional[pd.DataFrame]): Internal data storage.
    """

    name: str = "TopicAnalysis"
    meta_data_file: str
    topic_data_file: str
    uncertainty_data_file: str
    meta_columns: Union[List[str], Dict[str, str]]
    topic_columns: Union[List[str], Dict[str, str]]
    uncertainty_columns: Union[List[str], Dict[str, str]]
    id_col: str = "id"
    timestamp_col: str = "timestamp"
    text_col: str = "text"
    frequency: str = "M"
    rolling_window: int = 3
    _data_: Optional[pd.DataFrame] = None
    _agg_data_: Optional[pd.DataFrame] = None

    @property
    def data(self) -> pd.DataFrame:
        """Merge three dataframes and return the result."""
        # Implement logic to merge meta_data_file, topic_data_file, and uncertainty_data_file
        # based on the selected columns and renaming if necessary.
        if self._data_ is None:
            meta_data = self._load_data(self.meta_data_file, self.meta_columns)
            topic_data = self._load_data(self.topic_data_file, self.topic_columns)
            uncertainty_data = self._load_data(
                self.uncertainty_data_file, self.uncertainty_columns
            )
            self._data_ = (
                meta_data.merge(topic_data, on=self.id_col)
                .merge(uncertainty_data, on=self.id_col)
                .dropna()
            )
            self._data_.set_index(self.timestamp_col, inplace=True)
        return self._data_

    def _load_data(
        self,
        data_file: str,
        columns: Union[List[str], Dict[str, str]],
    ) -> pd.DataFrame:
        """Load data from the three files."""
        data = HyFI.load_dataframe(data_file)
        if isinstance(columns, list):
            data = data[columns]
        elif isinstance(columns, dict):
            data = data[columns.keys()]
            data.rename(columns=columns, inplace=True)
        return data

    def aggregate(
        self,
        frequency: Optional[str] = "M",
    ) -> pd.DataFrame:
        """Aggregate data by a given frequency.

        Args:
            frequency (str): Frequency for aggregation (e.g., 'D' for daily, 'M' for monthly).

        Returns:
            pd.DataFrame: Aggregated data.
        """
        return self.data.groupby(pd.Grouper(freq=frequency)).mean()

    @property
    def agg_data(self) -> pd.DataFrame:
        """Aggregate data by a given frequency."""
        if self._agg_data_ is None:
            self._agg_data_ = self.aggregate(self.frequency)
        return self._agg_data_

    def rolling_average(
        self,
        rolling_window: Optional[int] = 3,
    ) -> pd.DataFrame:
        """Calculate rolling average with a given window size.

        Args:
            window (int): Window size for rolling average. Default is 3.

        Returns:
            pd.DataFrame: Data with rolling average applied.
        """
        return self.agg_data.rolling(rolling_window).mean()

    def plot(
        self,
        columns: List[str],
        rolling_window: Optional[int] = 3,
        title: Optional[str] = None,
        xlabel: Optional[str] = "Date",
        ylabel: Optional[str] = None,
        xtick_every: Optional[int] = None,
    ) -> None:
        """Plot selected columns with rolling average.

        Args:
            columns (List[str]): Columns to plot.
            rolling_window (int): Window size for rolling average. Default is 3.
            title (str): Plot title.
            xlabel (str): X-axis label.
            ylabel (str): Y-axis label.
        """
        data = self.rolling_average(rolling_window)
        data.plot(y=columns, figsize=(20, 10))
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
            (self.data.index >= start_date) & (self.data.index <= end_date)
        ]
        columns = columns or [self.id_col, self.text_col, topic]
        return data.sort_values(topic, ascending=False).head(n)
