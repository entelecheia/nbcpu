# Methodology

## Overview

Measuring central bank policy uncertainty involves gauging the uncertainty related to the monetary policy decisions taken by central banks, such as changes in interest rates, reserve requirements, or other monetary tools. These are several common approaches used:

**1. Textual Analysis of Central Bank Communications:** This involves analyzing the communications made by central banks, including minutes of the meetings, speeches, reports, press releases, and other forms of communication. The textual content can be analyzed manually or using automated natural language processing techniques. Researchers may look for keywords related to uncertainty or employ more sophisticated techniques, such as topic modeling or sentiment analysis, to quantify the level of uncertainty. For instance, the Baker, Bloom, and Davis EPU index uses this approach.

**2. Financial Market-based Measures:** These measures use financial market data to infer the level of policy uncertainty. The assumption is that financial markets incorporate all available information, including the perceived uncertainty about future monetary policy. Examples of such measures include options-implied volatility measures such as the VIX index, which captures the market's expectation of future volatility, and the MOVE index, which specifically measures the volatility in U.S. Treasury markets.

**3. Surveys of Professional Forecasters:** Another approach is to conduct surveys of professional economic forecasters and use their responses to measure policy uncertainty. This could involve questions about the expected future path of policy rates or other monetary policy actions. The dispersion or disagreement among forecasters' responses can then be used as a measure of uncertainty.

**4. Econometric Models:** Econometric models, like the GARCH model (Generalized Autoregressive Conditional Heteroskedasticity), are also used to measure policy uncertainty. These models estimate volatility in economic variables that might be affected by central bank policies, such as inflation or exchange rates.

**5. Machine Learning Techniques:** With advancements in technology, machine learning techniques are increasingly being used to measure policy uncertainty. For instance, Support Vector Machines, Logistic Regression, or Neural Networks can be used to classify and tag documents relevant to policy uncertainty.

## The Merits of Topic-based Methods

The topic-based method of measuring economic uncertainty has several strengths relative to other methods:

1. **Comprehensiveness:** Unlike methods that rely on specific keywords, a topic-based approach analyzes the entire mixture of words in an article, providing a more holistic view of the content and theme of the article. This allows for a comprehensive understanding of the context in which uncertainty is discussed.

2. **Flexibility:** It's not reliant on the presence of specific pre-determined keywords, which can sometimes lead to false positives (an article might contain all the keywords but not actually be about the specific type of uncertainty being measured) or false negatives (an article could be discussing a topic of uncertainty without using the specific keywords).

3. **Disambiguation:** Topic-based methods can differentiate between different types of uncertainty, allowing for more nuanced analysis. For instance, this method can differentiate between uncertainty related to "economic and financial distress", "institutional framework of monetary policy", "Norway’s relationship with the EU", and "technology and firm expansion".

4. **Correlation with other measures:** There are positive correlations between the topic-based uncertainty measures and other established uncertainty proxies such as the US VIX and realized stock market volatility, suggesting that this method is valid and reliable.

However, it's worth noting that topic-based methods also have limitations. The process of assigning labels based on the topic correlations may be subjective, and the measures may not capture all forms of uncertainty, especially those not frequently discussed in the news media. As with any method, topic-based measures are one tool in the larger toolbox for analyzing economic uncertainty and are likely to be most effective when used in conjunction with other methods.

## Topic Modeling

Topic modeling is an unsupervised machine learning technique that automatically identifies the main topics in a collection of documents. It provides a way of uncovering hidden thematic patterns in the text and categorizing the documents based on these themes.

The output of topic modeling is a list of topics, each represented by a collection of words, and a weight or probability distribution over those words. Each document is then represented as a mixture of these topics. The idea is that certain combinations of words tend to appear together in documents on the same topic. For instance, a document about monetary policy might frequently use words like "interest", "rates", "central bank", and "inflation".

There are several algorithms used for topic modeling, but one of the most popular ones is Latent Dirichlet Allocation (LDA).

### Latent Dirichlet Allocation (LDA)

LDA is a generative probabilistic model that assumes each document is a mixture of a certain number of topics and each word in the document is attributable to one of the document's topics. The "latent" in LDA refers to the fact that the assignment of words to topics is not observed and needs to be inferred.

A generative model, such as Latent Dirichlet Allocation (LDA), tries to mimic the process of how the data was generated. In the context of text data and topic modeling, LDA attempts to reverse engineer the process by which a human might have written a collection of documents.

When a human writes an article or a document, they typically have several topics or themes in mind. For example, if a journalist is writing an article about monetary policy in Cambodia, they might want to discuss topics such as inflation, interest rates, and the role of the National Bank of Cambodia. The writer doesn't pick topics for each word randomly; instead, they have a distribution of topics in their mind, and words related to those topics are more likely to appear in the article.

In the process of writing, the author selects a topic based on their topic distribution and then writes down a word based on the word distribution of that topic. This process is repeated until the article is complete. This is the generative process that LDA tries to model.

LDA, as a generative model, attempts to go back from the observed data (the words in the documents) to the hidden parameters that might have generated this data (the topic mixtures for each document and the word distributions for each topic). It does this by assuming that documents are produced in the following way:

1. For each document, a mixture of topics is chosen from a Dirichlet distribution. Each topic is represented as a distribution over words.
2. For each word in the document, a topic is chosen from the document's topic mixture.
3. A word is chosen from the word distribution of the selected topic.

By working backwards from the observed documents, LDA can infer the hidden topic structure, providing insight into the underlying themes of the collection of documents. This makes LDA a powerful tool for uncovering the latent topics that pervade a large corpus of text.

**The Number of Topics**

One of the crucial decisions a researcher needs to make when using Latent Dirichlet Allocation (LDA) for topic modeling is deciding the number of topics (often denoted as "K") in the model. This choice highly impacts the results because it determines how granular the topics identified by the model will be.

If the number of topics is set too low, the model may produce broad, unspecific topics that are not very informative. On the other hand, if the number of topics is set too high, the model may produce very specific topics that only cover a small number of documents, or even split what is conceptually one topic into multiple topics.

Unfortunately, there is no surefire way to select the "correct" number of topics a priori. It often requires iterative trial and error, guided by the researcher's domain knowledge and the quality of the topics produced. To aid in this process, measures such as perplexity and topic coherence can be used.

**Topic Coherence**

Topic coherence is a measure of how semantically consistent the words in a topic are. It aims to quantify the degree to which a topic is interpretable and meaningful to humans. Topic coherence measures have been found to correlate well with human interpretability.

Several different measures of topic coherence exist, but they generally follow the same logic: topics containing words that frequently co-occur or are semantically similar should have high coherence, while topics with words that rarely co-occur or are semantically dissimilar should have low coherence. Some popular measures of topic coherence include:

1. **C_v measure**: This measure leverages a sliding window to capture the semantic similarity of word pairs and normalize indirect confirmation measures. It is widely used due to its superior performance compared to other coherence measures.

2. **U_mass measure**: It is based on document co-occurrence and a sliding window. It measures the co-occurrence of pairs of words in the same window.

High coherence scores suggest that the words within a given topic co-occur more frequently, making the topic more interpretable and, thus, more useful.

## The Output of Topic Modeling

The output of the LDA model will provide two primary components relevant to the research study: topic-word distributions and document-topic distributions.

**Topic-Word Distributions:**

A topic-word distribution is a matrix that indicates the probability of a word being part of a particular topic. This distribution allows us to understand the composition of each topic. In the context of this research, it provides insights into the primary themes discussed in the context of Cambodia's monetary policy.

For example, a topic might include words such as "dollarization", "riel", "exchange rate", and "currency" with high probabilities, which could indicate a theme focused on currency management. Alternatively, a topic might include words like "inflation", "price stability", and "consumer price index", pointing to a topic centered on price stability concerns.

**Document-Topic Distributions:**

The document-topic distribution is a matrix that indicates the probability of a document (or in this case, a news article) being about a certain topic. This distribution allows us to understand which topics are discussed in each news article.

In the context of this research, it can give a sense of the main themes addressed in each article, and by extension, it can provide insights into what aspects of monetary policy were of primary concern at different points in time. For example, if many articles around a certain date have a high probability for a topic related to inflation, it could suggest that inflation concerns were particularly salient at that time.

Furthermore, the temporal trends in these topic probabilities can give insights into the evolution of monetary policy uncertainty over time. If the probabilities for certain topics increase during periods of economic instability or major policy changes, it would suggest that these topics contribute to monetary policy uncertainty.

### Estimation of LDA and Identification of Uncertainty Topics

Given the mathematical foundation of our LDA model, we further specify the methodology for identifying and quantifying uncertainty-related topics.

Firstly, we define a set of seed words related to uncertainty to guide the second LDA model. These seed words represent the inherent vocabulary of uncertainty and are used to initialize the topic-word distribution for the uncertainty-related topics.

The EM algorithm then comes into play to estimate both the topic-word and document-topic distributions. During the E-step, we calculate the posterior distribution of the topic assignments considering the observed words and the current estimates of the distributions:

$$p(z_{i,j}=k|\mathbf{w},\boldsymbol{\phi}^{(t)},\boldsymbol{\theta}^{(t)}) = \frac{\phi_{k,w_{i,j}}^{(t)} \theta_{i,k}^{(t)}}{\sum_{l=1}^K \phi_{l,w_{i,j}}^{(t)} \theta_{i,l}^{(t)}}$$

In the subsequent M-step, we update the estimates of the topic-word and document-topic distributions based on this posterior distribution:

$$\phi_{k,w}^{(t+1)} = \frac{\sum_{i=1}^M \sum_{j=1}^{N_i} w_{i,j} [z_{i,j}=k] p(z_{i,j}=k|\mathbf{w},\boldsymbol{\phi}^{(t)},\boldsymbol{\theta}^{(t)})}{\sum_{i=1}^M \sum_{j=1}^{N_i} [z_{i,j}=k] p(z_{i,j}=k|\mathbf{w},\boldsymbol{\phi}^{(t)},\boldsymbol{\theta}^{(t)})}$$

$$\theta_{i,k}^{(t+1)} = \frac{\sum_{j=1}^{N_i} [z_{i,j}=k] p(z_{i,j}=k|\mathbf{w},\boldsymbol{\phi}^{(t)},\boldsymbol{\theta}^{(t)})}{\sum_{j=1}^{N_i} \sum_{l=1}^K [z_{i,j}=l] p(z_{i,j}=l|\mathbf{w},\boldsymbol{\phi}^{(t)},\boldsymbol{\theta}^{(t)})}$$

With the aid of the indicator function $[z_{i,j}=k]$ which equals 1 when $z_{i,j}=k$ and 0 otherwise.

The algorithm iterates until convergence, after which we select the uncertainty-related topics as those with the highest probabilities of containing at least one of the seed words.

Finally, to quantify uncertainty, we compute an 'uncertainty score' for each document. This score is derived as the sum of the probabilities of the uncertainty-related topics in the document. Thus, a document with a higher uncertainty score signifies a higher level of policy uncertainty.

This method of identifying and quantifying uncertainty-related topics underpins the second LDA model for measuring the intensity of policy uncertainty.

## Quantifying Uncertainty

Quantifying policy uncertainty in Cambodia's highly dollarized economy necessitates a nuanced and multifaceted approach. Recognizing the complexity of this task, our research employs a dual-model approach, utilizing two separate Latent Dirichlet Allocation (LDA) models. The first model categorizes the topics of policy uncertainty, while the second measures the intensity of the uncertainty. This dual-model approach provides a comprehensive understanding of central bank policy uncertainty in the context of the National Bank of Cambodia.

1. **Topic Classification Model (Model 1):**

   The first LDA model is designed to classify potential topics representing key areas of policy uncertainty. These areas include Exchange Rate Policy Uncertainty, Currency Stabilization Policy Uncertainty, De-dollarization Policy Uncertainty, and Impact of International Monetary Policy Uncertainty. The model is initialized with seed words corresponding to these topics, guiding the model to learn a vocabulary associated with these areas of interest. The number of topics ($K$) is set higher than four, allowing the model to explore a broader set of topics. Subsequent analysis identifies the learned topics most related to the policy areas of interest.

2. **Uncertainty Intensity Model (Model 2):**

   The second LDA model focuses on measuring the intensity of uncertainty within articles. This model is initialized with a predefined set of seed words related to uncertainty, guiding the topic modeling process. The 'uncertainty score' for each document is computed as the sum of the probabilities of the uncertainty-related topics within the document. A higher uncertainty score signifies a greater level of policy uncertainty within that document.

### Aggregation

The aggregation process transforms the uncertainty scores obtained from Model 2 into a time-series representation of policy uncertainty. This involves determining the time frame, normalizing the scores, aggregating them according to the chosen method (mean, median, or sum), applying smoothing techniques if necessary, and interpreting the final measure.

The dual-model approach allows for the creation of policy uncertainty indices that track the level of policy uncertainty in each category over time. For example, a monthly Exchange Rate Policy Uncertainty Index could be computed by averaging the uncertainty scores of all articles classified under that category in each month. Similar indices could be created for other categories.

This approach provides valuable insights into the specific sources of policy uncertainty and how these evolve over time. It captures not only the overall level of policy uncertainty but also how this uncertainty is distributed across different policy areas. The relative weight of uncertainty-related topics in an article is indicative of the intensity of uncertainty, an assumption validated by comparing the results with other indicators of policy uncertainty.

However, the robustness of the findings should be verified by applying different topic modeling parameters and checking for consistency in the results. This ensures that the approach is tailored to the unique monetary landscape of Cambodia, reflecting the complexities associated with assessing policy uncertainty in a highly dollarized economy.
