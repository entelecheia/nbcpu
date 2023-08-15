# %%
from nbcpu import HyFI

meta_file = "/home/yjlee/workspace/projects/nbcpu/workspace/datasets/processed/khmer_tokenized/train.parquet"
uncertainty_file = "/home/yjlee/workspace/projects/nbcpu/workspace/nbcpu-topic_uncertainty/model/outputs/LDA_model(4)_k(20)-doc_topic_dists.parquet"
topic_file = "/home/yjlee/workspace/projects/nbcpu/workspace/nbcpu-topic_prior/model/outputs/LDA_model(1)_k(20)-doc_topic_dists.parquet"

# load meta data
meta = HyFI.load_dataframe(meta_file)
meta = meta[["id", "time", "title", "text"]]

# load topic and uncertainty data
uncertainty_data = HyFI.load_dataframe(uncertainty_file)
uncertainty_data = uncertainty_data[["id", "topic0", "topic1"]]
uncertainty_data.rename(
    columns={"topic0": "uncertainty", "topic1": "improve"}, inplace=True
)

topic_data = HyFI.load_dataframe(topic_file)
topic_data = topic_data[["id", "topic0", "topic1", "topic7"]]
topic_data.rename(
    columns={"topic0": "econ", "topic1": "banking", "topic7": "asean"}, inplace=True
)

infer_file = "/home/yjlee/workspace/projects/nbcpu/workspace/nbcpu-topic_uncertainty_filtered/model/outputs/inferred_topics/LDA_model(2)_k(5)-inferred_doc_topic_dists.parquet"
infer_data = HyFI.load_dataframe(infer_file)
infer_data = infer_data[["id", "topic0", "topic1", "topic2"]]
infer_data.rename(
    columns={"topic0": "risk", "topic1": "mitigation", "topic2": "mp"}, inplace=True
)

# merge all together
data = (
    meta.merge(topic_data, on="id")
    .merge(uncertainty_data, on="id")
    .merge(infer_data, on="id")
)

# %%
# aggregate by time (monthly) and plot
import matplotlib.pyplot as plt

weight_data = data[["time", "uncertainty", "improve", "econ", "banking", "asean"]]
# starting from 2017-01
weight_data = weight_data[weight_data["time"] >= "2017-01-01"]
weight_data["period"] = weight_data["time"].dt.to_period("M")
agg_data = weight_data.groupby(["period"]).mean().reset_index()
# rolling average 3 months
# agg_data = agg_data.rolling(3).mean()
agg_data.plot(y=["uncertainty", "econ"], figsize=(20, 10))
xticks = agg_data["period"].dt.strftime("%Y-%m").tolist()
# every 6 months
xticks = [xticks[i] if i % 6 == 0 else "" for i in range(len(xticks))]
plt.xticks(range(len(xticks)), xticks)
plt.show()

# %%
# proportion of econ topic documents (econ weight > 0.5)
econ_data = data[data["econ"] > 0.6]
uncertain_econ_data = econ_data[econ_data["risk"] > 0.5]
econ_data["period"] = econ_data["time"].dt.to_period("M")
uncertain_econ_data["period"] = uncertain_econ_data["time"].dt.to_period("M")

agg_data = uncertain_econ_data.groupby(["period"]).count().reset_index()
# divide by total number of documents
total_count = data.groupby(["period"]).count().reset_index()
agg_data["econ"] = agg_data["econ"] / total_count["econ"]
agg_data.plot(y=["id"], figsize=(20, 10))

# %%
total_count.plot(y=["id"], figsize=(20, 10))
# %%
# %%
econ_data = data[data["econ"] > 0.5]
weight_data = econ_data[["time", "risk", "econ", "mitigation", "mp", "banking"]]
# starting from 2017-01
weight_data = weight_data[weight_data["time"] >= "2017-01-01"]
weight_data["time"] = weight_data["time"].dt.to_period("M")
agg_data = weight_data.groupby(["time"]).mean().reset_index()
# rolling average 3 months

agg_data.plot(y=["econ", "risk", "mp", "mitigation"], figsize=(20, 10))
xticks = agg_data["time"].dt.strftime("%Y-%m").tolist()
# every 6 months
xticks = [xticks[i] if i % 6 == 0 else "" for i in range(len(xticks))]
plt.xticks(range(len(xticks)), xticks)
plt.show()
# %%
agg_data[["risk"]].rolling(3).mean().plot(figsize=(20, 10))
xticks = agg_data["time"].dt.strftime("%Y-%m").tolist()
# every 6 months
xticks = [xticks[i] if i % 6 == 0 else "" for i in range(len(xticks))]
plt.xticks(range(len(xticks)), xticks)
plt.show()
# %%
