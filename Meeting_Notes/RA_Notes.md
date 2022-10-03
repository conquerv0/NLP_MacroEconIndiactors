## RA-Notes

# Part I. Data Processing & Pipeline Setup

### 1.1 Toolkit & Documentation

> Query: Elastic Search, a SQL-like query tool
1. Proquest TDM Account
2. Text & Datamining tools. https://mdl.library.utoronto.ca/technology/text-and-data-mining-software/text-and-data-mining-tools-overview

   
### 1.2  VPN & Server Access

> SSN: Public-Private Key

1. VPN access
2. Server

### 1.3 Metadata Issues

1. Store data in a CSV
2. Update the info 

> 6.22 Update: 
1. Issues with "Terms": Store the whole terms for now in case the need for further processing arises. 

> 7.06 Update:
1. Put in Printlocation Infomation, such as DocEdition, ColumnHeader, DocSection. [reference(1546074706)]
2. For any missing metadata information, fill in NAs. 

> 7.12 Update:
1. `Extract_Meta`: Store every header in seperate pandas row, then 
2. `Term_Info`: Maybe instead of collecting every information, store the information as a dictionary to retain the structure. 

### 1.4 Metadata Search on Keywords

1. Running search based on keywords
2. Sentiment analysis
3. Training / Validation with Advanced Models
4. Use doc id to join different files
5. End output should be a single files corresponding to different keywords, respectively.

### 1.5 Sentiment Analysis

1. Average scores might not be accurate 
2. Find some metrics to gauge the overall tone for the journal/article. 
    - Subjectivity
    - Polarity
    - Overall Scores: Normalizing the scores over the sentences. 

### 2.1 Deployment on Server Environment

> Standardize the extraction, cleaning, NER and sentiment analysis on the server to make sure no details are missed testing on the small dataset.
1. Try to run `text_mining.ipynb` on TDM server. 
2. Do a search to get what we already have. (Parameters: AN)


### 2.0 Testing the efficiency/complexity of Mining-Analysis

1. Running this on a metadata search with 1-Month time span
2. 

# Part II. Analysis with Comparision of various Dataset

### 1.1 General Direction
> July 27th Update: 
1. Issues with missing packages (SpaCy and Textblob) on TDM
2. Perform test with "Yellen (), Google (), Hitler (800k) ", Includes the Global News Stream and the Historical Newspaper. 
3. Create a sentiment test comparison with different chairs of Federal Reserve, relating to the time period. 
4. Create temporal sentiment analysis on `Google` . We can also make some comparison with another Internet Giant, `AltaVista` and `Yahoo` (which can provides sentimental analysis view during period of their competition). 

## 1.2. Next Step: (Aug 10th)
> Further checking:
1. Make sure that TDM recognize the exact context
2. Sample some paper snippets in the dataset to make sure the mined result is not outside of our interest. (ex: 'google' being used as a verb rather than referring to the company. )
3. There might be "migration" of a concept moving from sources to sources(ex: 'gay' was mainly in poetry 100 years ago, but now appear in motion pictures, law, newspaper, etc.)

> Further Analysis
1. Run a `trend line` to demonstrate how the sentiment evolves overtime. 
2. We can identify short term spikes in the time series. 
3. Separate the data segment into country-based demographic so that we can identify difference in sentiment. 

## 1.3 Fall Update(Sep 9th):

> Problem encountered:
1. Datasets contain confounding variables, ex. Google was not exactly mentioned in terms of the company. (ProQuest indexed every 'Google' word mentioned as 'Google LLC')
2. Continue trendline analysis in the internet company segments?

> Potential Solution:
1. Extract words to the left/right of the Company name to understand the contexts of the texts. (create a helper function that adjust this 'context_window_extraction'). 
2. Establish baseline scripts so the module can be adapated to explore other topics. 

> Potential exploration:
1. Sentiments in geographic location
2. Finding political affliation/endorsement with sentiment of the article. We can potentially build metrics evaluating these political dimensions in our analysis. 

## 1.4 Time Series

1. Daily
2. Monthly Data: Stock
3. Quarter: Business Cycle
4. Annual

Notes: 
1. Newspaper also provides a geography tags that can be traced back further along in the history. 
2. Make sure to include the '0' in the time series, do not drop it.  