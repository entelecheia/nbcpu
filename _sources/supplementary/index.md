# Supplementary Materials

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

### Detailed Workflow

1. **Crawling:** Fetches the required data based on the specified configuration.
2. **Processing:** Includes preprocessing tasks such as filtering datasets based on specific criteria.
3. **Topic Modeling:** Runs different topic modeling tasks, including those with and without prior information.
4. **Analysis:** Conducts analysis on the derived topics, including uncertainty filtering and inference.

The package also contains the code for the experiments, serving as a reference for implementing similar research.

```{tableofcontents}

```
