<!--next-version-placeholder-->

## v0.8.0 (2023-08-10)

### Feature

* **pipeline:** Add dataframe eval columns ([`25e3d26`](https://github.com/entelecheia/nbcpu/commit/25e3d2657c8435e1939537316853894cdd411360))
* **pipeline:** Add new data filter and eval functions to datasets config ([`43e13e9`](https://github.com/entelecheia/nbcpu/commit/43e13e9df2601dbe4a376b882ab3c4e540033ad8))
* **config:** Add datasets-tokenize pipeline ([`5760a07`](https://github.com/entelecheia/nbcpu/commit/5760a07b34209448874e8a25ab43ea1123e05d22))
* **pipeline:** Add datasets-save configuration file ([`8c60c2a`](https://github.com/entelecheia/nbcpu/commit/8c60c2abeb39bb189288aa35dd3cde6c4c6e8669))

## v0.7.0 (2023-08-08)

### Feature

* **pipeline:** Enable extract_tokens in datasets configuration ([`25a09b2`](https://github.com/entelecheia/nbcpu/commit/25a09b2eb30a16d03b258690b04a0888b646bf7a))
* **tokenizer:** Add new nbcpu configuration, add nbcpu stopwords assets ([`4a89af6`](https://github.com/entelecheia/nbcpu/commit/4a89af6c61385c1f6fc6be0dbf155d4ad8441536))

## v0.6.0 (2023-08-04)

### Feature

* **pipeline:** Add pipe_tokenize to datasets-test.yaml and datasets.yaml ([`439eaa8`](https://github.com/entelecheia/nbcpu/commit/439eaa851dcb8de79a087a9a7e7a8ca2e5218821))
* **nbcpu:** Add lexikanon to plugins ([`9c08de9`](https://github.com/entelecheia/nbcpu/commit/9c08de9d6f874f0cb17e0f7bdd14030bf1d326e5))
* **pyproject.toml:** Add lexikanon dependency ([`8f6f444`](https://github.com/entelecheia/nbcpu/commit/8f6f444dc5a93018334d591db98e80c16fb71028))
* **pipeline:** Add datasets-test configuration ([`d657675`](https://github.com/entelecheia/nbcpu/commit/d657675673825ed5cfe18556d0d26aa7e6f58202))
* **config:** Add datasets.yaml configuration for pipeline ([`712a229`](https://github.com/entelecheia/nbcpu/commit/712a2293b5a80906f6ecffbe16c38273ba269572))
* **config/task:** Add datasets configuration file ([`3919fde`](https://github.com/entelecheia/nbcpu/commit/3919fdecc5dfafd2b13e7a8e4261d7b1d2f8defa))

## v0.5.0 (2023-07-29)

### Feature

* **fetcher:** Add delay_between_requests option to khmer configuration ([`7a76281`](https://github.com/entelecheia/nbcpu/commit/7a76281de67aeefc65caf7fbd4d89a6c5d5e5a63))
* **config/fetcher:** Add new configuration file for Phnompenh keywords search ([`ebe3dbf`](https://github.com/entelecheia/nbcpu/commit/ebe3dbf17d5a697124d79b0cb5df403e6d368279))
* **fetcher:** Add phnompenh fetcher ([`46f3f3e`](https://github.com/entelecheia/nbcpu/commit/46f3f3e7a0446316d26ad3781e706249facb573d))
* **nbcpu/fetcher:** Add delay between requests parameter to phnomphen fetcher, remove snippet from parse page links function ([`ddce346`](https://github.com/entelecheia/nbcpu/commit/ddce346f4e45bf35383b7c24eef81543234a082c))
* **nbcpu/fetcher:** Add delay between requests functionality, consolidate article metadata assembly, add user agent to headers ([`d15204c`](https://github.com/entelecheia/nbcpu/commit/d15204c57f6e204bfd347f67c165df28da85a19b))
* **fetcher:** Add delay between requests configuration ([`5da36f1`](https://github.com/entelecheia/nbcpu/commit/5da36f11cde56bd500bb2d04d8361c5ef57121b5))
* **nbcpu/fetcher:** Add delay between requests in phnompenh.py ([`b81ca72`](https://github.com/entelecheia/nbcpu/commit/b81ca721285e628bb0b682e411726c594492b92e))
* **fetcher:** Add start_page to khmer.yaml configuration ([`9d4bfdf`](https://github.com/entelecheia/nbcpu/commit/9d4bfdff98f1c14eac2a150a1932d44976c1e7c3))
* **fetcher:** Add PhnompenhFetcher for Phnom Penh Post articles ([`08eb8bd`](https://github.com/entelecheia/nbcpu/commit/08eb8bdc8fda628d312b96dc9ee73e2c43636fa0))
* **nbcpu/fetcher:** Add start_page property in BaseFetcher class, use encoded keywords for searching and crawling ([`f2ddb13`](https://github.com/entelecheia/nbcpu/commit/f2ddb13dc93ed42e2e552eb96c8c77889a76f487))
* **fetcher:** Add start_page to phnompenh configuration ([`e550bcb`](https://github.com/entelecheia/nbcpu/commit/e550bcb443c975502d70ea0b6c64b44199d2d546))
* **tests:** Add test_phnompenh_fetcher.py for nbcpu fetcher testing ([`197adba`](https://github.com/entelecheia/nbcpu/commit/197adba6927a81eb0cd2c2bc4b24e1708275bbd9))
* **fetcher:** Add new configuration file for PhnompenhFetcher ([`6c0e4c1`](https://github.com/entelecheia/nbcpu/commit/6c0e4c15b1d17d81ab319c0a24e6d3ca663bdb2c))
* **fetcher:** Implement base fetcher functionalities for crawling and scraping articles ([`f4fae2e`](https://github.com/entelecheia/nbcpu/commit/f4fae2eb5d5d726d56cc404d09f59f42cfce1563))

### Documentation

* **literature:** Correct reference year for Azqueta-Gavaldón, update heading format ([`74860ce`](https://github.com/entelecheia/nbcpu/commit/74860ce6ff474e1c0e3ea63fc0e56a143b25a5cc))
* **book/paper:** Add references.md ([`5a8d8de`](https://github.com/entelecheia/nbcpu/commit/5a8d8decc46ad851fe8bdb1776343880f5235160))
* **book:** Add references to the table of contents ([`94c334c`](https://github.com/entelecheia/nbcpu/commit/94c334ce40acb23c0ae71295a630848a9c0b768a))

## v0.4.0 (2023-07-29)

### Feature

* **config:** Add new fetcher-test workflow configuration ([`fae1e9f`](https://github.com/entelecheia/nbcpu/commit/fae1e9f7be0b4e50a3a5f4185fd2fc8c64791abb))
* **data:** Add nbcpu installation and usage in khmer notebook ([`c393ec2`](https://github.com/entelecheia/nbcpu/commit/c393ec21141bd8ff11a73272c0d553192d1a43d9))
* **book:** Add new sections in chapter, update table of contents structure ([`d295823`](https://github.com/entelecheia/nbcpu/commit/d295823502bafba08706eb2ad58b482177b256fb))

### Fix

* **dependencies:** Upgrade hyfi to 1.12.5 ([`3a3acac`](https://github.com/entelecheia/nbcpu/commit/3a3acac94082a0c7f4b54b9ec75394608cf908c2))
* **dependencies:** Upgrade hyfi to 1.12.4 ([`c5e7747`](https://github.com/entelecheia/nbcpu/commit/c5e7747c3b93b4bf27f281dab0c2a9cd59f33c8e))

### Documentation

* **khmer.ipynb:** Add Overview and Results sections, include an Example snippet ([`5bb1ac1`](https://github.com/entelecheia/nbcpu/commit/5bb1ac1ef0d8b9ffc250bceffdc8c2621c9c7891))

## v0.3.0 (2023-07-28)

### Feature

* **khmer:** Add multiprocessing ([`e3293d6`](https://github.com/entelecheia/nbcpu/commit/e3293d68d2be198ea1d7c8cff0f56c10e826db40))

### Fix

* **khmer:** Handle spaces in keyword query, correct arguments in append_to_jsonl call ([`dc79d98`](https://github.com/entelecheia/nbcpu/commit/dc79d98c116f12cb6bcbf85da917361faeb66f1a))

## v0.2.0 (2023-07-28)

### Feature

* **fetcher:** Add Khmer fetcher configuration ([`1be2a5e`](https://github.com/entelecheia/nbcpu/commit/1be2a5eaf67bee15bf2334768de1cbc0fb37fa53))
* **fetcher:** Add output_dir to fetcher config ([`f064b54`](https://github.com/entelecheia/nbcpu/commit/f064b54055964caa70599e08144c5185ee95c757))
* **fetcher:** Add khmer-all configuration ([`4a8640f`](https://github.com/entelecheia/nbcpu/commit/4a8640f0f41784d0802ccdbe728145f70bc7865b))
* **config:** Add new workflow fetcher configuration ([`f5ce165`](https://github.com/entelecheia/nbcpu/commit/f5ce1654566e8c2e70a4feed45b8815c5e87fed0))
* **nbcpu/fetcher:** Add fetch method to khmer fetcher ([`77963a2`](https://github.com/entelecheia/nbcpu/commit/77963a222fe3a338bf0ab8c92fed7cfcd7d6c5de))
* **nbcpu:** Add new configuration files ([`bb7f560`](https://github.com/entelecheia/nbcpu/commit/bb7f560930deb94e07bc704f5a2cfa866082b626))
* **tests:** Add KhmerFetcher tests in nbcpu module ([`6da5add`](https://github.com/entelecheia/nbcpu/commit/6da5add6c29b714ddafaeab8801196624127e95d))
* **nbcpu/fetcher:** Add KhmerFetcher class and fetching methods ([`33da9de`](https://github.com/entelecheia/nbcpu/commit/33da9dea94e2dc96f939aa563e9a370e7451f0ba))
* **khmerFetcher:** Add new configuration for Khmer fetcher ([`a9cabdc`](https://github.com/entelecheia/nbcpu/commit/a9cabdc01c7ce10be123feeb108ba5bc89e9fbf4))

### Fix

* **dependencies:** Upgrade hyfi to 1.12.2 ([`bb3ed2f`](https://github.com/entelecheia/nbcpu/commit/bb3ed2f713fa8eed7cc74a5d9e50cc321726a6a9))
* **khmer:** Handle case for max_num_articles as None ([`378e10f`](https://github.com/entelecheia/nbcpu/commit/378e10f625c38982beefb01de9eaaadbb8b39ad4))

## v0.1.2 (2023-07-28)

### Fix

* **pyproject.toml:** Remove version_pattern from configuration ([`946fcb9`](https://github.com/entelecheia/nbcpu/commit/946fcb96408b5011cb660ee9b0efbf530d463da8))
* **dependencies:** Update hyfi to 1.12.1 ([`cb7e6d7`](https://github.com/entelecheia/nbcpu/commit/cb7e6d71a1d88daa88a2a64afdbe8c054d7123d1))
* **nbcpu:** Remove unused imports and optimize package initializati, enhance package information and logger initialization ([`9229bf5`](https://github.com/entelecheia/nbcpu/commit/9229bf53e426147b1c9214ddbc890eb647874947))
* **dependencies:** Upgrade hyfi to 1.12.0 ([`5be50f0`](https://github.com/entelecheia/nbcpu/commit/5be50f0415fe3569cdcb6287869be4c626c4eccc))

## v0.1.1 (2023-06-28)

### Fix

* **README:** Update codecov badge token ([`7d3af23`](https://github.com/entelecheia/nbcpu/commit/7d3af231ed57d982c4efc9b724dfbc0d6e35ba4e))

## v0.1.0 (2023-06-28)

### Feature

* Initial version ([`707bef3`](https://github.com/entelecheia/nbcpu/commit/707bef3ad95da9ada63ae6b5e73f1f4e0281fef4))
