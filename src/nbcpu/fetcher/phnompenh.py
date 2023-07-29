"""Phnom Penh Post Fetcher."""
from datetime import datetime
from functools import partial
from typing import List, Optional

import requests
from bs4 import BeautifulSoup
from hyfi.main import HyFI

from .base import BaseFetcher

logger = HyFI.getLogger(__name__)


class PhnompenhFetcher(BaseFetcher):
    """
    Fetcher for Phnom Penh Post.
    """

    _config_name_: str = "phnompenh"
    _config_group_: str = "fetcher"
    output_dir: str = f"workspace/datasets/{_config_group_}/{_config_name_}"

    start_page: int = 0
    delay_between_requests: float = 20.0
    search_url: str = "https://phnompenhpost.com/search/node/{keyword}?page={page}"
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

    def encode_keyword(self, keyword: str):
        return keyword.replace(" ", "%20")

    def fetch_links(self):
        parse_page_func = partial(
            _parse_page_links,
            print_every=self.print_every,
            verbose=self.verbose,
        )
        self._fetch_links(parse_page_func)

    def fetch_articles(self):
        self._fetch_articles(_parse_article_text)


def _parse_page_links(
    page_url: str,
    header: Optional[dict] = None,
    print_every: int = 10,
    verbose: bool = False,
) -> Optional[List[dict]]:
    """Get the links from the given page."""
    links = []
    try:
        if header is None:
            header = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
            }
        response = requests.get(page_url, headers=header)
        # Check if page exists (status code 200) or not (status code 404)
        if response.status_code == 404:
            logger.info("Page [%s] does not exist, stopping...", page_url)
            return None
        soup = BeautifulSoup(response.text, "html.parser")

        # Check if page exists (has search results) or not
        search_results = soup.find("ol", class_="search-results node-results")
        if not search_results:
            logger.info("Page [%s] does not have search results, stopping...", page_url)
            return None

        # Find all articles within the search results
        articles = search_results.find_all("li", class_="search-result")

        for item_no, item in enumerate(articles):
            # Extract and store article information
            title = item.find("h3", class_="title").text.strip()
            url = item.find("a")["href"]
            date_str = (
                item.find("div", class_="posted-date").span.text.split("by")[0].strip()
            )
            date = datetime.strptime(date_str, "%d %b %Y")
            # snippet = item.find("p", class_="search-snippet").text.strip()

            if verbose and item_no % print_every == 0:
                logger.info("Date: %s", date.isoformat())
                logger.info("Title: %s", title)
                logger.info("URL: %s", url)
            link = {
                "title": title,
                "url": url,
                "date": date.isoformat(),
            }
            links.append(link)
    except Exception as e:
        logger.error("Error while fetching the page url: %s", page_url)
        logger.error(e)
    return links


def _parse_article_text(
    url: str,
    header: Optional[dict] = None,
) -> Optional[dict]:
    """Parse the article text from the given divs."""
    try:
        if header is None:
            header = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
            }
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.text, "html.parser")

        if article_body_div := soup.find("div", itemprop="articleBody"):
            # Find all p tags within the div
            p_tags = article_body_div.find_all("p")

            # Extract the text from each p tag and join them together
            article_text = "\n".join(p_tag.text for p_tag in p_tags)
            return {
                "text": article_text,
            }
    except Exception as e:
        logger.error("Error while scraping the article url: %s", url)
        logger.error(e)
    return None
