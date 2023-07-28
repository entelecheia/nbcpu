import json
import multiprocessing as mp
from datetime import datetime
from functools import partial
from pathlib import Path
from typing import List, Optional

import requests
from bs4 import BeautifulSoup
from hyfi.composer import BaseModel
from hyfi.main import HyFI

logger = HyFI.getLogger(__name__)


class KhmerFetcher(BaseModel):
    """
    Fetcher for Khmer Times.
    """

    _config_name_: str = "khmer"
    _config_group_: str = "fetcher"

    search_url: str = "https://www.khmertimeskh.com/page/{page}/?s={keyword}"
    search_keywords: List[str] = [
        "NBC",
        "Exchange Rate",
        "De-dollarization",
        "Inflation",
        "GDP",
        "Monetary Policy",
        "Finance",
        "Banking",
        "Stock Exchange",
        "Uncertain",
        "Economic",
        "Policy",
        "Financial",
        "Riel",
        "Bank",
        "Economy",
        "Securities Exchange",
        "National Bank of Cambodia",
    ]
    max_num_pages: Optional[int] = 2
    max_num_articles: Optional[int] = 10
    output_dir: str = "workspace/datasets/khmer"
    link_filename: str = "links.jsonl"
    article_filename: str = "articles.jsonl"
    overwrite_existing: bool = False
    num_workers: int = 1
    print_every: int = 10
    verbose: bool = True

    _links: List[dict] = []
    _articles: List[dict] = []

    def __call__(self):
        self.fetch()

    def fetch(self):
        self.fetch_links()
        self.fetch_articles()

    @property
    def links(self):
        return self._links or self._load_links()

    @property
    def articles(self):
        return self._articles or self._load_articles()

    @property
    def link_filepath(self) -> str:
        _path = Path(self.output_dir) / self.link_filename
        _path.parent.mkdir(parents=True, exist_ok=True)
        return str(_path)

    @property
    def article_filepath(self) -> str:
        _path = Path(self.output_dir) / self.article_filename
        _path.parent.mkdir(parents=True, exist_ok=True)
        return str(_path)

    @property
    def link_filepath_tmp(self) -> str:
        _path = Path(self.output_dir) / f"{self.link_filename}.tmp"
        _path.parent.mkdir(parents=True, exist_ok=True)
        return str(_path)

    @property
    def article_filepath_tmp(self) -> str:
        _path = Path(self.output_dir) / f"{self.article_filename}.tmp"
        _path.parent.mkdir(parents=True, exist_ok=True)
        return str(_path)

    def _load_links(self):
        if Path(self.link_filepath).exists():
            self._links = load_jsonl(self.link_filepath)
        return self._links

    def _load_articles(self):
        if Path(self.article_filepath).exists():
            self._articles = load_jsonl(self.article_filepath)
        return self._articles

    def fetch_links(self):
        num_workers = min(self.num_workers, len(self.search_keywords))
        self._load_links()
        links = self._links
        if num_workers > 1:
            self._fetch_links_mp(num_workers, links)
        else:
            for keyword in self.search_keywords:
                self._links = crawl_khmer_times(
                    keyword,
                    search_url=self.search_url,
                    links=links,
                    max_num_pages=self.max_num_pages,
                    link_filepath=self.link_filepath_tmp,
                    print_every=self.print_every,
                    verbose=self.verbose,
                )
        original_len = len(self._links)
        self._links = remove_duplicates(self._links, key="url")
        logger.info(
            "Removed %s duplicate links from %s links",
            original_len - len(self._links),
            original_len,
        )
        save_jsonl(self._links, self.link_filepath)
        logger.info("Saved %s links to %s", len(self._links), self.link_filepath)

    def _fetch_links_mp(self, num_workers, links):
        process_batch_partial = partial(
            crawl_khmer_times,
            search_url=self.search_url,
            links=links,
            max_num_pages=self.max_num_pages,
            link_filepath=self.link_filepath_tmp,
            print_every=self.print_every,
            verbose=self.verbose,
        )
        with mp.Pool(num_workers) as pool:
            results = pool.map(process_batch_partial, self.search_keywords)
        links = []
        for result in results:
            links.extend(result)
        self._links = links

    def fetch_articles(self):
        num_workers = self.num_workers
        self._load_articles()
        articles = self._articles
        if num_workers > 1:
            self._fetch_articles_mp(num_workers, articles)
        else:
            self._articles = scrape_article_text(
                self.links,
                articles=articles,
                overwrite_existing=self.overwrite_existing,
                max_num_articles=self.max_num_articles,
                article_filepath=self.article_filepath_tmp,
                print_every=self.print_every,
                verbose=self.verbose,
            )
        original_len = len(self._articles)
        self._articles = remove_duplicates(self._articles, key="url")
        logger.info(
            "Removed %s duplicate articles from %s articles",
            original_len - len(self._articles),
            original_len,
        )
        save_jsonl(self._articles, self.article_filepath)
        logger.info(
            "Saved %s articles to %s", len(self._articles), self.article_filepath
        )

    def _fetch_articles_mp(self, num_workers, articles):
        batch_size = len(self.links) // num_workers
        batches = [
            self.links[i : i + batch_size]
            for i in range(0, len(self.links), batch_size)
        ]
        process_batch_partial = partial(
            scrape_article_text,
            articles=articles,
            overwrite_existing=self.overwrite_existing,
            article_filepath=self.article_filepath_tmp,
            max_num_articles=self.max_num_articles,
            print_every=self.print_every,
            verbose=self.verbose,
        )
        with mp.Pool(num_workers) as pool:
            results = pool.map(process_batch_partial, batches)
        articles = []
        for result in results:
            articles.extend(result)
        self._articles = articles


def crawl_khmer_times(
    keyword: str,
    search_url: str = "https://www.khmertimeskh.com/page/{page}/?s={keyword}",
    links: Optional[List[dict]] = None,
    max_num_pages: Optional[int] = 2,
    link_filepath: Optional[str] = None,
    print_every: int = 10,
    verbose: bool = False,
) -> List[dict]:
    """Crawl Khmer Times for article links with the given keyword.

    Args:
        keyword (str): Keyword to search for.
        search_url (str, optional): URL to search for the keyword. Defaults to "https://www.khmertimeskh.com/page/{page}/?s={keyword}".
        links (List[dict], optional): List of links to append to. Defaults to None.
        max_num_pages (Optional[int], optional): Maximum number of pages to crawl. Defaults to 2.
        link_filepath (Optional[str], optional): Filepath to save the links to. Defaults to None.
        print_every (int, optional): Print progress every n pages. Defaults to 10.
        verbose (bool, optional): Print progress. Defaults to False.

    Returns:
        List[dict]: List of links.
    """

    page = 1
    article_no = 0  # Number of articles found
    links = links or []
    link_urls = [link["url"] for link in links]
    logger.info("Fetching links for keyword: %s", keyword)
    while max_num_pages is None or page <= max_num_pages:
        keyword = keyword.replace(" ", "+")
        page_url = search_url.format(page=page, keyword=keyword)

        response = requests.get(page_url)
        # Check if page exists (status code 200) or not (status code 404)
        if response.status_code == 404:
            logger.info("Page %s does not exist, stopping...", page)
            break

        try:
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the section with class 'section-category'
            section = soup.find("section", class_="section-category")

            # Find all articles within the section
            articles = section.find_all("article")

            for article in articles:
                article_no += 1
                # Extract and print article information
                title = article.find("h2", class_="item-title").text
                url = article.find("a")["href"]
                if verbose and article_no % print_every == 0:
                    logger.info("[Keyword: %s] Page: %s", keyword, page)
                    logger.info("Title: %s", title)
                    logger.info("URL: %s", url)
                if url not in link_urls:
                    link = {
                        "title": title,
                        "url": url,
                        "keyword": keyword,
                    }
                    links.append(link)
                    link_urls.append(url)
                    if link_filepath:
                        append_to_jsonl(link, link_filepath)
                else:
                    logger.info("Link %s already exists, skipping...", url)
        except Exception as e:
            logger.error("Error while fetching the page url: %s", page_url)
            logger.error(e)

        page += 1

    logger.info("Finished fetching links for keyword: %s", keyword)
    logger.info("Total links fetched: %s", len(links))
    return links


def scrape_article_text(
    links: List[dict],
    articles: Optional[List[dict]] = None,
    overwrite_existing: bool = False,
    max_num_articles: Optional[int] = 10,
    article_filepath: Optional[str] = None,
    print_every: int = 10,
    verbose: bool = False,
) -> List[dict]:
    """Scrape the article text from the given links.

    Args:
        links (List[dict]): List of links to scrape.
        articles (Optional[List[dict]], optional): List of articles to append to. Defaults to None.
        overwrite_existing (bool, optional): Overwrite existing articles. Defaults to False.
        max_num_articles (Optional[int], optional): Maximum number of articles to scrape. Defaults to 10.
        article_filepath (Optional[str], optional): Filepath to save the articles to. Defaults to None.
        print_every (int, optional): Print progress every n articles. Defaults to 10.
        verbose (bool, optional): Print progress. Defaults to False.

    Returns:
        List[dict]: List of articles.
    """
    articles = articles or []
    article_urls = [article["url"] for article in articles]
    for i, link in enumerate(links):
        if max_num_articles is not None and i >= max_num_articles:
            logger.info("Reached max number of articles, stopping...")
            break

        url = link["url"]
        title = link["title"]
        keyword = link["keyword"]
        if url in article_urls and not overwrite_existing:
            logger.info("Article [%s](%s) already exists, skipping...", title, url)
            continue

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the div with class 'entry-content'
            entry_content_div = soup.find("div", class_="entry-content")

            # Find the div with class 'entry-meta'
            entry_meta_div = soup.find("div", class_="entry-meta")

            if entry_content_div and entry_meta_div:
                article = parse_article_text(
                    entry_content_div,
                    entry_meta_div,
                    url=url,
                    keyword=keyword,
                    title=title,
                )
                articles.append(article)
                article_urls.append(url)
                if article_filepath:
                    append_to_jsonl(article, article_filepath)
                if verbose and (i + 1) % print_every == 0:
                    logger.info("Article [%s](%s) scraped", title, url)
            else:
                logger.info("Article [%s](%s) does not exist, skipping...", title, url)
        except Exception as e:
            logger.error("Error while scraping the article url: %s", url)
            logger.error(e)

    logger.info("Finished scraping articles")
    logger.info("Total articles scraped: %s", len(articles))
    return articles


def parse_article_text(
    entry_content_div,
    entry_meta_div,
    url: str,
    keyword: str,
    title: str,
) -> dict:
    """Parse the article text from the given divs."""
    # Find all p tags within the div and extract the text
    p_tags = entry_content_div.find_all("p")
    article_text = "\n".join(p_tag.text for p_tag in p_tags)

    # Extract the entry categories
    entry_categories = [a_tag.text for a_tag in entry_meta_div.find_all("a", rel="tag")]

    # Extract the entry time and convert it to a datetime object
    entry_time_str = entry_meta_div.find("time", class_="entry-time")["datetime"]
    entry_time = datetime.fromisoformat(entry_time_str)

    return {
        "url": url,
        "keyword": keyword,
        "title": title,
        "categories": entry_categories,
        "time": entry_time.isoformat(),  # Convert datetime to string
        "text": article_text,
    }


def append_to_jsonl(data, filename: str, encoding: str = "utf-8") -> None:
    """Append a json payload to the end of a jsonl file."""
    json_string = json.dumps(data, ensure_ascii=False)
    with open(filename, "a", encoding=encoding) as f:
        f.write(json_string + "\n")


def load_jsonl(filename: str, encoding: str = "utf-8") -> List[dict]:
    """Load a jsonl file into a list of json objects."""
    with open(filename, "r", encoding=encoding) as f:
        return [json.loads(line) for line in f]


def save_jsonl(
    data: List[dict],
    filename: str,
    encoding: str = "utf-8",
) -> None:
    """
    Save a list of json objects to a jsonl file.
    """
    with open(filename, "w", encoding=encoding) as f:
        for line in data:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")


def remove_duplicates(data: List[dict], key: str) -> List[dict]:
    """Remove duplicates from a list of dicts based on a key."""
    seen = set()
    new_data = []
    for d in data:
        if d[key] not in seen:
            new_data.append(d)
            seen.add(d[key])
    return new_data
