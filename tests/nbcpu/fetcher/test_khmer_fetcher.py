from nbcpu.fetcher.khmer import KhmerFetcher


def test_save_hyfi_config():
    KhmerFetcher.save_hyfi_config()


def test_khmer_fetcher():
    khmer = KhmerFetcher(verbose=True)
    assert khmer.search_url == "https://www.khmertimeskh.com/page/{page}/?s={keyword}"
    khmer.fetch_links()
    khmer.fetch_articles()


if __name__ == "__main__":
    test_save_hyfi_config()
    # test_khmer_fetcher()
