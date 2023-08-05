from nbcpu.fetcher.khmer import KhmerFetcher


def test_generate_config():
    KhmerFetcher.generate_config()


def test_khmer_fetcher():
    khmer = KhmerFetcher(
        search_keywords=["NBC"],
        max_num_pages=1,
        max_num_articles=1,
        verbose=True,
        output_dir="workspace/test/khmer",
        overwrite_existing=True,
    )
    assert khmer.search_url == "https://www.khmertimeskh.com/page/{page}/?s={keyword}"
    khmer.fetch_links()
    khmer.fetch_articles()


if __name__ == "__main__":
    test_generate_config()
    test_khmer_fetcher()
