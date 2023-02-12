import requests
import pandas as pd
from bs4 import BeautifulSoup


def print_headlines(ticker):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'}
    url = 'https://www.bloomberg.com/search?query=' + ticker
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = [h.text for h in soup.find_all('a', class_='headline__3a97424275')]
    dates = [d.text for d in soup.find_all(class_="publishedAt__dc9dff8db4")]
    df = pd.DataFrame({"headlines": headlines, "dates": dates})
    print(df)


