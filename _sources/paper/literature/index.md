## Literature Review

Economic policy uncertainty, with implications for financial markets, economic performance, corporate investment, labor market dynamics, and political polarization, has garnered significant research interest ({cite:t}`Azqueta-gavaldon:2017`). Methods to measure uncertainty generally fall into three categories: financial measures, textual measures, and miscellaneous methods ({cite:t}`Kaveh-yazdy:2021`).

**Financial Measures**

These measures often utilize stock market volatility, such as the VIX index, or differences between expected and actual financial parameters ({cite:t}`Kaveh-yazdy:2021'). For instance, forecast errors in the stock market or discrepancies in expected and actual macroeconomic parameters, collected via surveys, are often employed to gauge uncertainty.

**Textual Measures**

Textual measures predominantly rely on documents, like monetary policy documents, and social media/news articles. They assess uncertainty by examining central bank minutes and gauge public sentiment towards uncertainty using social media posts and news articles ({cite:t}`Kaveh-yazdy:2021`). A notable early attempt at quantifying uncertainty through textual analysis was the Economic Policy Uncertainty (EPU) Index proposed by {cite:t}`Baker:2016`. This index measures the frequency of articles in major newspapers that contain certain uncertainty-related keywords, thus providing a quantifiable metric for policy uncertainty. The EPU index was subsequently expanded to include older newspaper archives, other countries, and specific policy category indices.

However, the manual process of article selection was cumbersome and paved the way for more efficient, unsupervised machine learning methods. For instance, Azqueta-Gavaldón used the Latent Dirichlet Allocation (LDA) to automate topic modeling in uncertainty measurement, providing a more efficient and flexible alternative to the EPU index ({cite:t}`Azqueta-gavaldon:2021`). Further advancements saw the adoption of more sophisticated machine learning techniques, such as support vector machines and logistic regression, for more accurate document classification and tagging ({cite:t}`Kaveh-yazdy:2021`).

**Topic-based Methods**

In response to the limitations of keyword-based methods, recent research like {cite:t}`Larsen:2021` proposed a topic-based method using Latent Dirichlet Allocation (LDA). This method categorizes articles based on their content and themes without the need for pre-training or labeling, allowing the entire word mixture in an article to contribute to theme identification. This approach offers several advantages, including the ability to differentiate between various types of uncertainty.

**Future Directions**

Despite these advances, there are still challenges to be overcome. The EPU index, while innovative, is criticized for being labor-intensive and difficult to update in real-time. Moreover, its application is primarily limited to advanced economies. To address these issues, Ahir et al. introduced the World Uncertainty Index (WUI), covering 143 countries. Furthermore, {cite:t}`Miranda-belmonte:2023` proposed a novel approach to estimate the subcategories of the EPU index using semantic clustering, word embeddings, and fuzzy k-means, facilitating real-time measurement and updating of the index.
