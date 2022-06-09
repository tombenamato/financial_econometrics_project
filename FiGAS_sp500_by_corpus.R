library(FiGASR)
library(stringr)

current_data_directory = paste(getwd(),"/data/sp500",sep = "")
path_to_id_csv = paste(current_data_directory, "/df_100stocks.csv", sep = "")
path_to_top_word = paste(current_data_directory, "/top_10_words_tfidf_proc_figass_by_corpus.csv", sep = "")
path_text = paste(current_data_directory, "/text", sep = "")
running_csv_file_name = "data/sp500/FiGAS_sp500_by_corpus.csv"
final_csv_file_name = "FiGAS_sp500_by_corpus_final.csv"

id_chosen = read.csv(file = path_to_id_csv)
id_chosen=  id_chosen[-1]
id_chosen = unlist(id_chosen)

top_words = read.csv(file = path_to_top_word)
top_words = top_words[!duplicated(top_words$article),]
rownames(top_words) = top_words$article
top_words = top_words[-1]
top_words = top_words[-1]
top_words = top_words[-1]

df = data.frame(id = 0, sent_score = 0)
for (folder in list.dirs(path_text)[-1]){
  for (file in list.files(paste(folder,"/", sep = ""), recursive = FALSE, include.dirs = FALSE)){
    # check if in set
    if (any(id_chosen==as.numeric(file))){
      file_path = paste(folder, "/",file, sep = "")
      text = readLines(file_path)
      text = paste(text[str_count(text, '\\w+')>3], collapse = "")
      text = list(text)
      # get ToI
      include = as.list(str_split(substr(top_words[file,1], 3, nchar(top_words[file,1]) - 3), "', '")[[1]])
      try(
        expr = {
          sentiment = get_sentiment(text = text, include = include)
          sent = sentiment[["sentiment_by_chunk"]][["Sentiment"]]
          sent = sent[sent!=0]
          # calculate mean only with important world that were really important, and that we obtain a value different from 0
          earning_sentiment_score = mean(sent)
          df[nrow(df)+1 ,] = c(file,earning_sentiment_score)
          write.csv(df, running_csv_file_name)
        }
      )
    }
  }
}
df = df[-1,] #remove first line of initialization


write.csv(df, final_csv_file_name)
