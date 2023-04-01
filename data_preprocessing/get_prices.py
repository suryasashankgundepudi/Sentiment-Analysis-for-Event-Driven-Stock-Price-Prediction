# Using yahoo finance for collecting stock prices
import yfinance as yf
from datetime import datetime
import os


def download_prices(filename="META", ticker="META"):
    today = datetime.today().date()
    data = yf.download(ticker, start="2016-01-01", end=today)
    directory = "../data/tickers/" + filename + "/"

    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Directory created successfully!")
    else:
        print("Directory already exists.")
    data.to_csv(directory + filename + ".csv")
    data.head()


