# Measuring Central Bank Policy Uncertainty

[![pypi-image]][pypi-url]
[![version-image]][release-url]
[![release-date-image]][release-url]
[![license-image]][license-url]
[![codecov][codecov-image]][codecov-url]
[![jupyter-book-image]][docs-url]

<!-- Links: -->

[codecov-image]: https://codecov.io/gh/entelecheia/nbcpu/branch/main/graph/badge.svg?token=P414TXNSHY
[codecov-url]: https://codecov.io/gh/entelecheia/nbcpu
[pypi-image]: https://img.shields.io/pypi/v/nbcpu
[license-image]: https://img.shields.io/github/license/entelecheia/nbcpu
[license-url]: https://github.com/entelecheia/nbcpu/blob/main/LICENSE
[version-image]: https://img.shields.io/github/v/release/entelecheia/nbcpu?sort=semver
[release-date-image]: https://img.shields.io/github/release-date/entelecheia/nbcpu
[release-url]: https://github.com/entelecheia/nbcpu/releases
[jupyter-book-image]: https://jupyterbook.org/en/stable/_images/badge.svg
[repo-url]: https://github.com/entelecheia/nbcpu
[pypi-url]: https://pypi.org/project/nbcpu
[docs-url]: https://nbcpu.entelecheia.ai
[changelog]: https://github.com/entelecheia/nbcpu/blob/main/CHANGELOG.md
[contributing guidelines]: https://github.com/entelecheia/nbcpu/blob/main/CONTRIBUTING.md

<!-- Links: -->

**Quantifying Central Bank Policy Uncertainty in Cambodia: A Topic Modeling Approach**

- Documentation: [https://nbcpu.entelecheia.ai][docs-url]
- GitHub: [https://github.com/entelecheia/nbcpu][repo-url]
- PyPI: [https://pypi.org/project/nbcpu][pypi-url]

## Abstract

Understanding and measuring central bank policy uncertainty is vital for predicting economic outcomes, especially in economies like Cambodia, where monetary policy tools are underdeveloped and the economy is heavily dollarized. This study presents a comprehensive analysis of central bank policy uncertainty in Cambodia, employing a dual-model approach using Latent Dirichlet Allocation (LDA) to classify and measure the intensity of policy uncertainty across key areas such as exchange rate policy, currency stabilization, and de-dollarization. By leveraging articles from major Cambodian news outlets, collected and filtered through automated methods, the research creates a rich dataset spanning from 2014 to 2023. The study estimates the document-topic and topic-word distributions from this corpus of news articles, thereby deriving measures of policy uncertainty. Through a combination of narrative evaluation and comparison with established uncertainty measures, the research offers a robust evaluation of the topic-based uncertainty measures, providing valuable insights into the specific sources of policy uncertainty and their evolution over time. The findings contribute to the broader understanding of economic policy uncertainty in emerging economies and have potential applications in risk assessment, decision-making, policy formulation, and strategic planning. Future directions include integrating additional analytical layers such as sentiment analysis and machine learning predictions to achieve a more nuanced understanding of economic uncertainty. The insights derived from this study hold significant implications for economists, policymakers, investors, and business leaders, emphasizing the importance of this research in the context of Cambodia's unique monetary policy challenges.
Supplementary Materials

## Introduction

The research code is publicly available as a Python package named `nbcpu`, hosted on [GitHub](http://github.com/entelecheia/nbcpu) and published on [PyPI](https://pypi.org/project/nbcpu/). Built on the [Hydra Fast Interface (HyFI)](https://hyfi.entelecheia.ai) framework and integrated with plugins [ThematOS](https://thematos.entelecheia.ai) and [Lexikanon](https://lexikanon.entelecheia.ai), `nbcpu` offers a streamlined command-line interface for replicating the experiments described in this research.

## Installation

`nbcpu` requires Python 3.8 or higher and can be installed using the following command:

```bash
pip install -U nbcpu
```

## Usage

### Overview

The `nbcpu` package is designed to facilitate the entire workflow of the research, encompassing crawling, processing, topic modeling, and analysis. The interface is structured into four main parts, each corresponding to a specific phase of the research.

### Configuration

The configuration for `nbcpu` is located in the `src/nbcpu/conf` directory and is divided into several sub-configurations. The main configuration file, `nbcpu`, orchestrates the entire workflow and includes the following sections:

- **Defaults:** Specifies the default configurations for various tasks.
- **Tasks:** Lists the tasks to be executed, such as fetching data, filtering datasets, and running topic models.
- **Global Settings:** Defines global parameters like the number of workers and paths to datasets and workspace.

A snippet of the configuration file is provided below:

```yaml
## @package _global_
defaults:
  - __init__
  - /fetcher@khmer_all: khmer_all
  - /task@nbcpu-datasets: nbcpu-datasets
  - /runner@nbcpu-topic_noprior: nbcpu-topic_noprior
  - /task@nbcpu-datasets_noprior_filter: nbcpu-datasets_noprior_filter
  - /runner@nbcpu-topic_prior: nbcpu-topic_prior
  - /runner@nbcpu-topic_uncertainty: nbcpu-topic_uncertainty
  - /task@nbcpu-datasets_uncertainty_filter: nbcpu-datasets_uncertainty_filter
  - /runner@nbcpu-topic_uncertainty_filtered: nbcpu-topic_uncertainty_filtered
  - override /project: nbcpu

_config_name_: nbcpu
verbose: false
tasks:
  - khmer_all
  - nbcpu-datasets
  - nbcpu-topic_noprior
  - nbcpu-datasets_noprior_filter
  - nbcpu-topic_prior
  - nbcpu-topic_uncertainty
  - nbcpu-datasets_uncertainty_filter
  - nbcpu-topic_uncertainty_filtered

nbcpu-topic_uncertainty_filtered:
  calls:
    - train
    - infer
  infer_args:
    model_config_file: ${__project_root_path__:}/workspace/nbcpu-topic_uncertainty_filtered/model/configs/model(2)_config.yaml
  corpus_to_infer:
    text_col: tokens
    data_load:
      data_file: ${__project_root_path__:}/workspace/datasets/processed/topic_noprior_filtered/train.parquet

global:
  num_workers: 100
  datasets_path: ${__get_path__:datasets}
  workspace_path: ${__project_workspace_path__:}
```

### Running Experiments

The entire workflow can be executed with the following command:

```bash
nbcpu +workflow=nbcpu
```

This command triggers the sequence of tasks defined in the configuration, including data fetching, preprocessing, topic modeling, and uncertainty analysis.

## Changelog

See the [CHANGELOG] for more information.

## Contributing

Contributions are welcome! Please see the [contributing guidelines] for more information.

## License

This project is released under the [MIT License][license-url].
