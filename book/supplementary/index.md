# Supplemental material

All the code for this research is available on [GitHub](http://github.com/entelecheia/nbcpu) and is pulished as a standalone Python package on [PyPI](https://pypi.org/project/nbcpu/). The package is called `nbcpu` and can be installed with `pip install nbcpu`.

Built upon the [Hydra Fast Interface (HyFI)](https://hyfi.entelecheia.ai) framework along with plugins, [ThematOS](https://thematos.entelecheia.ai) and [Lexikanon](https://lexikanon.entelecheia.ai), the package provides a simple command-line interface for running the experiments described in this research. The package also contains the code for the experiments, which can be used as a reference for implementing similar experiments.

## Installation

The package can be installed with `pip install nbcpu`. The package requires Python 3.8 or higher.

## Usage

The package provides a command-line interface for running the experiments. The interface is built upon the [Hydra Fast Interface (HyFI)](https://hyfi.entelecheia.ai) framework. The interface is divided into four main parts: crawling, preprocessing, topic modeling, and analysis. Refer to each sub section for more details.

The entire workflow comprises of the several sub configurations and packed into a single configuration called `nbcpu`. The configuration is located in the `src/nbcpu/conf` directory. The configuration is divided into several sub configurations, each of which is located in the `src/nbcpu/conf` directory.

```yaml
# @package _global_
defaults:
  - __init__
  - /fetcher@khmer_all: khmer_all
  - /task@nbcpu-datasets: nbcpu-datasets
  - /task@nbcpu-dataset_noprior_filter: nbcpu-dataset_noprior_filter
  - /task@nbcpu-dataset_uncertainty_filter: nbcpu-dataset_uncertainty_filter
  - /runner@nbcpu-topic_noprior: nbcpu-topic_noprior
  - /runner@nbcpu-topic_prior: nbcpu-topic_prior
  - /runner@nbcpu-topic_uncertainty: nbcpu-topic_uncertainty
  - /runner@nbcpu-topic_uncertainty_filtered: nbcpu-topic_uncertainty_filtered
  - override /project: nbcpu

_config_name_: nbcpu
verbose: true
tasks:
  - khmer_all
  - nbcpu-datasets
  - nbcpu-topic_noprior
  - nbcpu-dataset_noprior_filter
  - nbcpu-topic_prior
  - nbcpu-topic_uncertainty
  - nbcpu-dataset_uncertainty_filter
  - nbcpu-topic_uncertainty_filtered

nbcpu-topic_uncertainty_filtered:
  calls:
    # - train
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

To run the entire workflow, run the following command:

```bash
nbcpu +workflow=nbcpu
```

```{tableofcontents}

```
