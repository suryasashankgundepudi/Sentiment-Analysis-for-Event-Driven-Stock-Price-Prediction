from data_preprocessing.collect_reuters import *
from data_preprocessing.get_prices import *
from data_preprocessing.combine_head_stock import *
import argparse
import os


parser = argparse.ArgumentParser(description='Sentiment analyzer')

parser.add_argument('-a', action="store_true", default=False)

parser.add_argument('--ticker', type=str, default= "META", help='Path to the text file.')

args = parser.parse_args()

print(args.ticker)
#run_headlines(args.ticker)
#download_prices(ticker)
#combine_headlines(ticker)
