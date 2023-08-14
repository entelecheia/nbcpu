<!--next-version-placeholder-->

## v0.12.0 (2023-08-14)

### Feature

* **nbcpu:** Add topic_uncertainty_filtered task in workflow configuration ([`245abbf`](https://github.com/entelecheia/nbcpu/commit/245abbf3457072668fdbe180d4f4069e73384e63))
* **nbcpu-dataset:** Add sample_data to pipeline ([`d021340`](https://github.com/entelecheia/nbcpu/commit/d021340b6b98f5e2e8f76cf6641c637b714d3c83))

## v0.11.0 (2023-08-14)

### Feature

* **tests:** Add new stopwords to nbcpu-uncertainty_filtered.txt ([`8ffe65c`](https://github.com/entelecheia/nbcpu/commit/8ffe65c54b35b4aab9d6033e81555ae1f9f6b1e6))
* **book:** Add uncertainty docs to data preprocessing ([`2f57aa6`](https://github.com/entelecheia/nbcpu/commit/2f57aa66be998c14284d1337a86fd4f614fbfaa1))
* **nbcpu:** Add new tasks and runners for uncertainty filtering ([`918fd35`](https://github.com/entelecheia/nbcpu/commit/918fd351494d4f26702bf579365480776571ea22))
* **tests:** Add 'provide' to stopwords list ([`2ae326f`](https://github.com/entelecheia/nbcpu/commit/2ae326f3ee31c045906026b6819cb7f1d55231f3))
* **nbcpu:** Add topic uncertainty filter to pipeline configuration ([`2836d55`](https://github.com/entelecheia/nbcpu/commit/2836d55a75b6b3aa64e5b7ee5f1211df5faa0f1c))
* **dataset:** Add nbcpu-topic_uncertainty_filtered configuration ([`b8915dd`](https://github.com/entelecheia/nbcpu/commit/b8915dddb163790ee5f261d7a9af74e1eb0e286f))
* **tests:** Add word_prior_uncertainty yaml file ([`157a3cb`](https://github.com/entelecheia/nbcpu/commit/157a3cbde8d3f2a4d0a8ebb34b41327b913ec3c8))
* **nbcpu:** Add topic_uncertainty runner ([`11b5fd0`](https://github.com/entelecheia/nbcpu/commit/11b5fd057f7a89f167bb3adff6f0ec891c7047b1))
* **nbcpu-topic_uncertainty.yaml:** Add new configuration file ([`2500dcd`](https://github.com/entelecheia/nbcpu/commit/2500dcdf91f455ec080bfb21f04ba4a2a411416e))
* **nbcpu:** Add topic uncertainty model configuration ([`5dcbb23`](https://github.com/entelecheia/nbcpu/commit/5dcbb2368dc04b2a0c7bbf74716169c20ec704a9))
* **dataset:** Add nbcpu-topic_uncertainty configuration ([`2445539`](https://github.com/entelecheia/nbcpu/commit/2445539f3c29f17b4d31dcd52288078394019fd2))
* **tests/assets:** Add stopwords/nbcpu-uncertainty.txt ([`065d011`](https://github.com/entelecheia/nbcpu/commit/065d011c94eeb1c779397f120fd0880d873125fb))
* **nbcpu-topic_noprior_filter:** Add dataframe_select_columns step, add merge_dataframes step ([`e9f39f0`](https://github.com/entelecheia/nbcpu/commit/e9f39f0e6595a3de00e6995cfd0914f8540afca3))
* **nbcpu-topic_prior:** Add dataset corpus override ([`091905c`](https://github.com/entelecheia/nbcpu/commit/091905ceae833d0ce660588772c71d0d23f3c631))

## v0.10.0 (2023-08-13)

### Feature

* **nbcpu-conf:** Add new dataset configuration file ([`ebe8fb0`](https://github.com/entelecheia/nbcpu/commit/ebe8fb0472fa3ab29650b0cf9a554e74321c8d2e))
* **nbcpu-topic_noprior_filter:** Add new evaluation column for irrelevant topics ([`7fe8e2c`](https://github.com/entelecheia/nbcpu/commit/7fe8e2cc36cd1a5839bfecf732a2b41f044dd95a))
* **pipeline:** Add additional filter step in nbcpu-topic_noprior_filter.yaml ([`0088c07`](https://github.com/entelecheia/nbcpu/commit/0088c075b6a0435d20f15b814475280134308e88))
* **nbcpu:** Add nbcpu-topic_noprior_filter task ([`c5c5a08`](https://github.com/entelecheia/nbcpu/commit/c5c5a088a93261bc51c7cf408b4fda373371b667))
* **nbcpu:** Add topic_noprior_filter configuration ([`0febe00`](https://github.com/entelecheia/nbcpu/commit/0febe00a81c986940cfa664921ebaf0d1b7ada35))
* **nbcpu-topic_noprior_filter:** Add new configuration file ([`1028d0f`](https://github.com/entelecheia/nbcpu/commit/1028d0fc2fdb4f22596ba47a899e8f3d1e83a0e4))
* **pipeline:** Add load_dataframe to nbcpu-datasets.yaml ([`4fe52ce`](https://github.com/entelecheia/nbcpu/commit/4fe52ce3bdaaa3c27450a56f3c03a25fa8ca0234))

## v0.9.0 (2023-08-13)

### Feature

* **tests:** Add new stopwords file for nbcpu uncertainty ([`b0b7935`](https://github.com/entelecheia/nbcpu/commit/b0b7935e06864ca49196f8d836a362e3310b433b))
* **tests:** Add new stopwords file for nbcpu-topic ([`08cbd5d`](https://github.com/entelecheia/nbcpu/commit/08cbd5de447366eff11c282271b8bcd47f8f3528))
* **tests:** Add nbcpu-tokenizer test asset ([`b7849ba`](https://github.com/entelecheia/nbcpu/commit/b7849bae13edf0a397467653dc82fa60f0130f9d))
* **nbcpu-topic_prior:** Add new configuration file ([`ce85f75`](https://github.com/entelecheia/nbcpu/commit/ce85f7506d2bf963cf97c27d1a7ee7454cedb697))
* **nbcpu:** Add new configuration for topic noprior model ([`e918f47`](https://github.com/entelecheia/nbcpu/commit/e918f47c5fc0f28bedb0d40351cc4cc6b82cd34c))
* **nbcpu:** Add new configuration for topic_prior model ([`8bce1b1`](https://github.com/entelecheia/nbcpu/commit/8bce1b19d12be4e8c4c146973555b8527fd401eb))
* **nbcpu-conf:** Add new nbcpu-topic_noprior configuration file ([`af7c5f2`](https://github.com/entelecheia/nbcpu/commit/af7c5f21161fefc008b238e24c14c66eaa3de88e))
* **topoc:** Add index file with stats ([`425c64e`](https://github.com/entelecheia/nbcpu/commit/425c64eb6f02e354efba95a3d04027564135ad6b))
* **nbcpu-topic_noprior.yaml:** Add new config file ([`64c9e63`](https://github.com/entelecheia/nbcpu/commit/64c9e638e3f89fe89888441448944937e68510a3))
* **dataset:** Add ngrams with max length 3 ([`ea8cf7d`](https://github.com/entelecheia/nbcpu/commit/ea8cf7d59c5139e41f65ac84a182b786b9c4938f))
* **tests:** Add new words to word_prior.yaml ([`6c255d9`](https://github.com/entelecheia/nbcpu/commit/6c255d912495c883f2d6a6d1f9adddf5fcf031a1))
* **nbcpu-topic_nouns:** Increase run_args and iterations, add train_summary_args ([`ea980ed`](https://github.com/entelecheia/nbcpu/commit/ea980ede85994cf7c428e8c53813847a5cce6e4b))
* **nbcpu-model:** Add additional configuration parameters ([`3dc75f1`](https://github.com/entelecheia/nbcpu/commit/3dc75f120ba82788680f8916854a06bb9e538080))
* **nbcpu:** Add nbcpu-topic task ([`1351d4b`](https://github.com/entelecheia/nbcpu/commit/1351d4bafff65760ec4ff8443aee6442002905e6))
* **nbcpu/conf/dataset:** Add new config file nbcpu-topic.yaml ([`ca18168`](https://github.com/entelecheia/nbcpu/commit/ca18168a0b516de99a63b67afb39a7301ac5e6f4))
* **nbcpu:** Create new nbcpu-topic.yaml configuration model ([`60112ac`](https://github.com/entelecheia/nbcpu/commit/60112ac0f13661fa8cbd03928d3bb78e88ba7aeb))
* **nbcpu-topic:** Add new configuration file ([`0715790`](https://github.com/entelecheia/nbcpu/commit/071579085eb3a9ec6dde1f0ad0ecb60bc4b1937b))
* **nbcpu-topic:** Add new configuration file ([`371176c`](https://github.com/entelecheia/nbcpu/commit/371176ccd87c6a5c02ff596ea4819de7710eaa71))
* **tests:** Add word_prior.yaml in assets/words ([`66d800d`](https://github.com/entelecheia/nbcpu/commit/66d800d4c42d12db34d831c6a016173297455b8c))
* **nbcpu:** Add thematos to plugins ([`bbc7c2f`](https://github.com/entelecheia/nbcpu/commit/bbc7c2ff51d929de32f6754c91a59a4e7183077f))
* **nbcpu:** Add new topic modeling configuration ([`6dec3b7`](https://github.com/entelecheia/nbcpu/commit/6dec3b785d454a000bf4aacfd109244124cc1033))
* **nbcpu:** Add new configuration file ([`4503099`](https://github.com/entelecheia/nbcpu/commit/4503099a76c488dbd77c0c2d669464bc267d9e0e))
* **nbcpu-datasets:** Add new configurations for data pipeline and tokenization ([`69aad65`](https://github.com/entelecheia/nbcpu/commit/69aad65c0c9ca1b0d13c135d6bf11dba8d7a2b48))
* **nbcpu:** Add new nbcpu-datasets configuration file ([`a9ca637`](https://github.com/entelecheia/nbcpu/commit/a9ca637a9968d2739dbc8bd0be18d7f97e7db00b))
* **nbcpu:** Add new tokenizer configuration ([`7ebdf16`](https://github.com/entelecheia/nbcpu/commit/7ebdf16c838725c107138d7381d4ff66ef522062))
* **config:** Add new nbcpu-test.yml configuration file ([`38ec41e`](https://github.com/entelecheia/nbcpu/commit/38ec41e79f611a53c3f83eb8933c85246809bfa1))
* **fetcher:** Add khmer_all configuration for data fetching ([`ff1d88e`](https://github.com/entelecheia/nbcpu/commit/ff1d88ec869683a6d95340eb0022196bcbc9d968))
* **nbcpu:** Add new project configuration file ([`5ad93d9`](https://github.com/entelecheia/nbcpu/commit/5ad93d90415600c2b8398469d06950a0a831905f))
* **dependencies:** Add thematos 0.9.0 ([`03fc521`](https://github.com/entelecheia/nbcpu/commit/03fc5217bfb83132332cc5ea2ca1ff92870b306e))

### Fix

* **tests:** Change 'rates' to 'rate' in word_prior.yaml ([`f813756`](https://github.com/entelecheia/nbcpu/commit/f813756c35cc53e8cba7f3468f3e93bb6ffcc28d))

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
