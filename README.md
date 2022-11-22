# NLP_MacroEconIndicators

## Phase 1: Meta Data: engineering and structuring

- [x]  Extract Meta
- [x]  Extract Text
- [x]  Keyword Search

## Phase 2: Time Series: how sentiment at an article level change over time

- [x]  Annual Sentiment Trend
- [x]  Monthly Sentiment Trend
- [x]  Daily Sentiment Trend
    - [x]  Summary statistics in a given time frame
    - [x]  Average reports, Time span, Variability Measures (in Month)
    - [ ]  Graph: Number of articles (Frequency Measure)
    - [ ]  Report the graph and table to Slack
        - [ ]  Long-horizon report
        - [ ]  Short trend report
- [ ]  Quarter Sentiment Trend

![Quarter_Mean](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f1decf11-eb02-46e3-a511-0ab0e0905b3e/Untitled.png)

![Quarter_Std](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bca79c2c-2899-4f3c-9a3b-02a756a681bd/Untitled.png)

## Phase 2: Time Series: how sentiment at an article level change over time

[Thesis Planning](https://www.notion.so/Thesis-Planning-e7fe4e5b943645d9bd7b62aebcd61745) 

- [ ]  Investigate Predictive Power of the sentiment

### Tools

- [ ]  Fin-BERT
    - The model is trained on financial statement, may not perform well on financial news
    - For stock-specific financial information might be good.
- TextBlob

[https://textblob.readthedocs.io/en/dev/](https://textblob.readthedocs.io/en/dev/)

- Time Series Model

[https://www.statsmodels.org/stable/tsa.html](https://www.statsmodels.org/stable/tsa.html)

[Research Resources](https://www.notion.so/2b890d6740b842a29de21f99cf109251)