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

### Preprocessing
pre-processing.ipynb  contains all the functions needed to download all the texts and also pre-process them.

### Topic Modeling 
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
### FiGAS sentiment analysis
Open one of the file in the FiGAS folder.

Change the parameters at the begining of the file.
#### Parameters
path_to_id_csv : The path to the csv file containing the id of the transcripts to analyse
path_to_top_word : The path to the csv file containing the topic words for each of the transcripts to analyse
path_text : The path to the folder containing the text of the Q&A transcripts part.
running_csv_file_name : The path of the ongoing csv containing the sentiment score for the transcripts will be save
final_csv_file_name : The path of the csv containing the sentiment score for the transcripts will be save

### FinBERT sentiment analysis
Open the file FinBert_final.ipynb

Goal : Run FinBERT on the transcripts to obtain deciles based on the sentiment scores (difference ratio). These deciles will be used to compute the abnormal returns.
       We count the number of sentence with neutral, positive and negative sentiment in each transcript, compute ratios (P/N ration, difference ratio) and form deciles based
       on these ratios.

#### Parameters
current_data_directory : The path folder containing all the transcripts in text format and the IDs of the transcripts to analyse
path_text : The path folder containing all the transcripts in text format
path_to_id_csv : The path to the csv file containing the IDs of the transcripts to analyse
N : number of transcripts that we want to analyse when we run FinBERT
start : index at which we want to start to analyze the N transcripts (must be comprised between 0 and 1300 s.t N + start <= 1300) 