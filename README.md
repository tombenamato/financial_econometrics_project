# Sentiment analysis of earning call transcripts
This Git regroups all of the resources to reproduce our results of our NLP earning call transcripts analysis and portfolio strategies.

## How to use the git
### Scrapping transcripts HTML 
Open the file scrapper_transcripts_html_specific_company.ipynb

Change the parameters in the parameters cell and run the notebook
#### Parameters
executable_path : The path to the chrome driver working on your os, use by selenium. For more details see selenium website.

ticker_html_path : The path of the directory for each company will be created and the html file downloaded

tickers : The list of tickers to dowlaod. We provide 2 function to obtain the sp500 and sp600 current tickers.

### Parsing HTML of earnings call transcript to obtain text file of the Q&A section
Open the file paser_transcript_page.ipynb

Change the parameters in the parameters cell and run the notebook
#### Parameters
dir_path_ticker : The path to the folder where html folders of companies to parse is.

dir_path_text : The path to the folder where the parsed transcripts are written.

### Select earnings call to analyse, from all dowloaded earning calls
Open the file select_earning_calls.

Change the parameters in the parameters cell and run the notebook

The notebook saves the earning calls to analyse in 'data/earning_call_dataframe in 2 files : one csv file with only earning call ids and one pickle file with all earning calls informations.

#### Parameters
sp : 'sp500' or 'sp600'

#### Preprocessing
pre-processing.ipynb  contains all the functions needed to download all the texts and also pre-process them.
#### Topic Modeling 
topic_modeling.ipynb aims to take as input the texts who have been processed and use it to find the most relevants topics and the words that are used for the sentimental analysis.

### NRC sentiment analysis
Open the file NRC/NRC.ipynb

Change the parameters in the parameters cell and run the notebook
#### Parameters
sp : 'sp500' or 'sp600'

### Calculate abnormal returns
Open the file abnormal_returns.ipynb

Change the parameters in the parameters cell and run the notebook

The notebook saves the abnormal graphs in data/abnormal_graphs.
#### Parameters
sp : 'sp500' or 'sp600'
