from collect_reuters import *
from get_prices import *
from combine_head_stock import *
ticker = "META"
run_headlines(ticker)
download_prices(ticker)
combine_headlines(ticker)
