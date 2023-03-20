from collect_reuters import *
from get_prices import *
from combine_head_stock import *

ticker = "APPLE"

print("Collecting Headlines for " + ticker)
run_headlines(ticker=ticker)
print("Downloading closing prices for " + ticker)
download_prices(filename=ticker, ticker="AAPL")
print("Adding price changes for " + ticker)
combine_headlines(ticker)
