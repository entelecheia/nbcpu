from datetime import datetime
from pathlib import Path
from typing import List, Optional

import requests
from bs4 import BeautifulSoup
from hyfi.composer import BaseModel
from hyfi.main import HyFI

logger = HyFI.getLogger(__name__)


class KhmerFetcher(BaseModel):
    _config_name_: str = "khmer"
    _config_group_: str = "fetcher"

    search_url: str = "https://www.khmertimeskh.com/page/{page}/?s={keyword}"
    search_keywords: List[str] = [
        "NBC",
        "National Bank of Cambodia",
        "Exchange Rate",
        "Economy",
        "Riel",
        "De-dollarization",
        "Inflation",
        "Monetary Policy",
        "Banking",
        "Finance",
        "Bank",
        "Financial",
        "Stock Exchange",
        "Uncertain",
        "Policy",
    ]
    max_num_pages: Optional[int] = 2
    max_num_articles: Optional[int] = 10
    output_dir: str = "workspace/datasets/khmer"
    link_filename: str = "links.json"
    article_filename: str = "articles.json"
    overwrite_existing: bool = False
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
    def link_filepath(self):
        _path = Path(self.output_dir)
        _path.mkdir(parents=True, exist_ok=True)
        return _path / self.link_filename

    @property
    def article_filepath(self):
        _path = Path(self.output_dir)
        _path.mkdir(parents=True, exist_ok=True)
        return _path / self.article_filename

    def _load_links(self):
        if self.link_filepath.exists():
            self._links = HyFI.load_json(self.link_filepath)
        return self._links

    def _load_articles(self):
        if self.article_filepath.exists():
            self._articles = HyFI.load_json(self.article_filepath)
        return self._articles

    def fetch_links(self):
        for keyword in self.search_keywords:
            self._links = crawl_khmer_times(
                keyword,
                search_url=self.search_url,
                links=self.links,
                max_num_pages=self.max_num_pages,
                print_every=self.print_every,
                verbose=self.verbose,
            )
            HyFI.save_json(self._links, self.link_filepath)
        logger.info("Saved %s links to %s", len(self._links), self.link_filepath)

    def fetch_articles(self):
        self._articles = scrape_article_text(
            self.links,
            articles=self.articles,
            overwrite_existing=self.overwrite_existing,
            max_num_articles=self.max_num_articles,
            print_every=self.print_every,
            verbose=self.verbose,
        )
        HyFI.save_json(self._articles, self.article_filepath)
        logger.info(
            "Saved %s articles to %s", len(self._articles), self.article_filepath
        )


def crawl_khmer_times(
    keyword: str,
    search_url: str = "https://www.khmertimeskh.com/page/{page}/?s={keyword}",
    links: Optional[List[dict]] = None,
    max_num_pages: Optional[int] = 2,
    print_every: int = 10,
    verbose: bool = False,
) -> List[dict]:
    """Crawl Khmer Times for article links with the given keyword.

    Args:
        keyword (str): Keyword to search for.
        search_url (str, optional): URL to search for the keyword. Defaults to "https://www.khmertimeskh.com/page/{page}/?s={keyword}".
        links (List[dict], optional): List of links to append to. Defaults to None.
        max_num_pages (Optional[int], optional): Maximum number of pages to crawl. Defaults to 2.
        print_every (int, optional): Print progress every n pages. Defaults to 10.
        verbose (bool, optional): Print progress. Defaults to False.

    Returns:
        List[dict]: List of links.
    """

    page = 1
    links = links or []
    link_urls = [link["url"] for link in links]
    logger.info("Fetching links for keyword: %s", keyword)
    while max_num_pages is None or page <= max_num_pages:
        page_url = search_url.format(page=page, keyword=keyword)

        response = requests.get(page_url)
        # Check if page exists (status code 200) or not (status code 404)
        if response.status_code == 404:
            logger.info("Page %s does not exist, stopping...", page)
            break

        soup = BeautifulSoup(response.text, "html.parser")

        # Find the section with class 'section-category'
        section = soup.find("section", class_="section-category")

        # Find all articles within the section
        articles = section.find_all("article")

        for article in articles:
            # Extract and print article information
            title = article.find("h2", class_="item-title").text
            url = article.find("a")["href"]
            if verbose and page % print_every == 0:
                logger.info("[Keyword: %s] Page: %s", keyword, page)
                logger.info("Title: %s", title)
                logger.info("URL: %s", url)
            if url not in link_urls:
                links.append(
                    {
                        "title": title,
                        "url": url,
                        "keyword": keyword,
                    }
                )
                link_urls.append(url)
            else:
                logger.info("Link %s already exists, skipping...", url)

        page += 1

    logger.info("Finished fetching links for keyword: %s", keyword)
    logger.info("Total links fetched: %s", len(links))
    return links


def scrape_article_text(
    links: List[dict],
    articles: Optional[List[dict]] = None,
    overwrite_existing: bool = False,
    max_num_articles: Optional[int] = 10,
    print_every: int = 10,
    verbose: bool = False,
) -> List[dict]:
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

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the div with class 'entry-content'
        entry_content_div = soup.find("div", class_="entry-content")

        # Find the div with class 'entry-meta'
        entry_meta_div = soup.find("div", class_="entry-meta")

        if entry_content_div and entry_meta_div:
            # Find all p tags within the div and extract the text
            p_tags = entry_content_div.find_all("p")
            article_text = "\n".join(p_tag.text for p_tag in p_tags)

            # Extract the entry categories
            entry_categories = [
                a_tag.text for a_tag in entry_meta_div.find_all("a", rel="tag")
            ]

            # Extract the entry time and convert it to a datetime object
            entry_time_str = entry_meta_div.find("time", class_="entry-time")[
                "datetime"
            ]
            entry_time = datetime.fromisoformat(entry_time_str)

            # Add the article text, entry categories, and entry time to the list
            articles.append(
                {
                    "url": url,
                    "keyword": keyword,
                    "title": title,
                    "categories": entry_categories,
                    "time": entry_time.isoformat(),  # Convert datetime to string
                    "text": article_text,
                }
            )
            article_urls.append(url)
            if verbose and (i + 1) % print_every == 0:
                logger.info("Article [%s](%s) scraped", title, url)
        else:
            logger.info("Article [%s](%s) does not exist, skipping...", title, url)

    logger.info("Finished scraping articles")
    logger.info("Total articles scraped: %s", len(articles))
    return articles
