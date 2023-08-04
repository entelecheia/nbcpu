from nbcpu.fetcher.phnompenh import PhnompenhFetcher


def test_generate_config():
    PhnompenhFetcher.generate_config()


def test_fetcher():
    phnompenh = PhnompenhFetcher(
        search_keywords=["NBC"],
        max_num_pages=1,
        max_num_articles=5,
        verbose=True,
        output_dir="workspace/test/phnompenh",
        overwrite_existing=True,
    )
    assert (
        phnompenh.search_url
        == "https://phnompenhpost.com/search/node/{keyword}?page={page}"
    )
    # phnompenh.fetch_links()
    # phnompenh.fetch_articles()


if __name__ == "__main__":
    test_generate_config()
    test_fetcher()
