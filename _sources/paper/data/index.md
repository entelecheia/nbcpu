# Data

## Data sources

- [Khmer Times](https://www.khmertimeskh.com/)
- [Phnom Penh Post](https://www.phnompenhpost.com/)

## Data Collection

For the purpose of this research, we will be utilizing articles from three major news outlets in Cambodia: Khmer Times and Phnom Penh Post. These sources were chosen for their relevance, comprehensiveness, and reputation as credible news platforms in Cambodia, providing a diverse range of coverage on the economic and financial matters of the country.

**1. Khmer Times**

Khmer Times is a major English language newspaper in Cambodia. It covers a wide range of topics, including domestic and international news, politics, business, lifestyle, and culture. The newspaper is known for its extensive coverage of economic issues, including the country's monetary policy.

**2. Phnom Penh Post**

The Phnom Penh Post is the oldest independent newspaper in Cambodia, offering both English and Khmer editions. It provides in-depth coverage of various topics, from politics to economy, lifestyle, and culture. It is particularly regarded for its detailed analysis of domestic economic affairs and policies.

We will gather articles from these sources using automated methods.

## Gathering the Raw Dataset

**Web Scraping:**

We will use web scraping tools to extract articles from the websites of the three news outlets. The Python libraries `BeautifulSoup` and `requests` will be particularly useful for this task. We will extract the headline, date, and full text of each article.

**Keyword Filtering:**

Once we have a comprehensive dataset of articles, we will filter the articles based on relevant keywords related to economic policy, such as "National Bank of Cambodia", "monetary policy", "exchange rate", "currency stabilization", "de-dollarization", and "U.S. Federal Reserve", among others. This will ensure we are only analyzing articles relevant to our research.

**Time Frame:**

We will determine a specific time frame for our study, and only gather articles published within this period. This will allow us to understand the evolution of policy uncertainty over a specified period of time.

This dataset will provide a rich source of information from which to analyze and measure the uncertainty surrounding Cambodia's central bank policy.

## Exploratory Data Analysis

We have collected 40,002 articles from the three news outlets. The articles were published between January 1, 2014 and July 31, 2023. After preprocessing, we are left with 39,632 articles.

### Yearly Distribution

The dataset spans from 2014 to 2023, with a total of 39,632 articles. The following observations can be made from the yearly distribution:

- **2014**: The dataset begins with 2,047 articles, having an average length of 3,345 words.
- **2015-2018**: A gradual increase in the number of articles is observed, reaching 3,530 in 2018, with average lengths ranging from 3,162 to 3,486 words.
- **2019-2020**: The number of articles continues to grow, reaching 4,688 in 2020, with average lengths around 3,400 words.
- **2021-2022**: A significant increase is noted, with 5,493 articles in 2021 and 6,866 in 2022, though the average length slightly decreases to around 3,100 words.
- **2023**: The data for 2023 includes 3,750 articles, with an average length of 3,255 words.

### Overall Trends

- **Number of Articles**: The dataset shows a consistent upward trend in the number of articles over the years, reflecting a growing interest in the subjects related to uncertainty, economics, and central bank policy.
- **Average Length**: The average length of the articles remains relatively stable, with minor fluctuations. The overall average length across all years is 3,247 words.

```{figure} ./figs/num_articles_trend.png
---
width: 80%
align: center
name: fig-num-articles-trend
---
Number of articles over time
```
