import yfinance as yf
from datetime import datetime
import os

os.chdir("/data preprocessing/")

today = datetime.today().date()


def download_prices(ticker="META"):
    data = yf.download(ticker, start="2016-01-01", end=today)
    data.to_csv("../data/" + ticker + ".csv")


