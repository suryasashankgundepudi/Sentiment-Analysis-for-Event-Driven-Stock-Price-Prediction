# data_preprocessing
Within this directory exists the files required to preprocess data for building a deep
neural network for sentiment analysis.

## `1. add_labels.py`
This code is using the vaderSentiment library to add sentiment labels to a file containing titles. The SentimentIntensityAnalyzer class is used to perform sentiment analysis on each title in the file.

The code starts by importing the SentimentIntensityAnalyzer class from the vaderSentiment library. Then, an instance of the class is created using the analyzer variable.

Next, the code reads the contents of a file called titles.txt and stores the lines in the lines variable.

The code then opens a new file called titles_new.txt and writes each line from the original file to the new file with a sentiment label added. The sentiment label is determined using the polarity_scores() method of the analyzer object. If the compound score is greater than or equal to 0.05, the label "@positive" is assigned. If the compound score is less than or equal to -0.05, the label "@negative" is assigned. Otherwise, the label "@neutral" is assigned.

Finally, the modified titles are written to the new file with the sentiment label attached using f.write(). The .strip() method is used to remove any extra whitespace from the line before adding the label.

## `2. collect_reuters.py`
This Python code scrapes news articles related to a given company from Reuters website, analyzes the sentiment of each article and stores the results in a Pandas dataframe. It uses Selenium and BeautifulSoup to scrape the website and Newspaper to extract the article text and title. The sentiment analysis is not done in this code but rather the article sentiment will be analyzed later. The final dataframe is then saved as a CSV and pickle file in a designated directory.

## `3. combine_head_stock`
This code reads in two dataframes from CSV files, one containing article headlines for a given stock ticker and the other containing stock price data for the same ticker. The code then merges the two dataframes based on the publishing date of each article and the corresponding stock price data. It calculates the price change for each article by comparing the stock price on the publication date with the stock price 30 days later. If the price has increased by 5% or more, it assigns a value of 1 (2 if the price increase was 10% or more), if the price has decreased by 5% or more, it assigns a value of -1 (-2 if the price decrease was 10% or more), and if the price has not changed by 5% or more, it assigns a value of 0. The resulting dataframe is then saved to a CSV file.

## `4. combine_titles.py`
This code reads in the contents of two text files, titles_new.txt and Sentences_AllAgree.txt, concatenates them, removes a specific string from the concatenated text, and then saves the resulting text to a new file named final_pre_training_data.txt.

## `5. creating_titles.py`
This code reads a folder containing TSV files with headlines and extracts the titles into a single output file. It first sets the output file name and mode (write). It then iterates over all files in the folder and checks if the file is a TSV file. If it is, it reads each line of the file and splits it into three components: timestamp, title, and URL. It then writes only the title to the output file, with each title on a new line. The output mode is set to "append" for subsequent writes to ensure that new titles are added to the end of the file. If an error occurs while reading a file line, a message is printed to inform the user.

## `6. get_prices.py`
This code defines a function called download_prices which uses the yfinance library to download historical stock prices for a given ticker symbol from Yahoo Finance. The function takes two optional parameters: filename (default value "META") and ticker (default value "META"). The downloaded data is then saved to a CSV file in a directory named after the filename parameter within a tickers subdirectory of the project's data directory. If the directory already exists, the function simply outputs a message saying so. Finally, the function returns the first few rows of the downloaded data.


## `7. run_all_data_files.py`
This code is a Python script that imports three functions from three separate Python files, and then runs them in sequence to collect headlines and stock prices for a specified company, and then combine the data.

The script starts by setting a value for ticker, which is used to specify the company to search for in Reuters and Yahoo Finance. It then calls the run_headlines function from collect_reuters.py to collect headlines for the specified company. After that, it calls the download_prices function from get_prices.py to download the closing prices for the same company from Yahoo Finance. Finally, it calls the combine_headlines function from combine_head_stock.py to combine the headlines and stock prices data for the specified company.
