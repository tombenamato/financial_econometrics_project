# Sentiment analysis of earning call transcripts
This Git regroups all of the resources to reproduce our results of our NLP earning call transcripts analysis and portfolio strategies.

## Link of the Google Drive with data:
https://drive.google.com/drive/folders/1-4Bj5yplrty2HqNq34AyTmdYMQahd7NB?usp=sharing

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
