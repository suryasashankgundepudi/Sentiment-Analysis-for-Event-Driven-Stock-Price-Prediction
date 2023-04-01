from collect_reuters import *
from get_prices import *
from combine_head_stock import *

# The name of the company when you search in Reuters
ticker = "APPLE"

# Collecting headlines for the stock
print("Collecting Headlines for " + ticker)
run_headlines(ticker=ticker)

# Collecting prices for the stock
print("Downloading closing prices for " + ticker)

# The second argument is the ticker in yahoo finance
download_prices(filename=ticker, ticker="AAPL")

# Adding price changes
print("Adding price changes for " + ticker)
combine_headlines(ticker)
