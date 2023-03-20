import yfinance as yf
from datetime import datetime
import os

os.chdir("D:/PYTHON3/Sentiment-Analysis-for-Event-Driven-Stock-Price-Prediction/data preprocessing/")

today = datetime.today().date()

ticker = "META"

data = yf.download(ticker, start="2016-01-01", end=today)

data.to_csv("../data/" + ticker + ".csv")


