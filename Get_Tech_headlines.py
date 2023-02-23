from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

# read in data and conduct basic data clean and rename columns
df=pd.read_csv(r'nasdaq_screener_1675799625051.csv',usecols=["Symbol","Name","Last Sale","Market Cap","Industry"])
df.columns = ["Symbol","Name","Last_Sale","Market_Cap","Industry"]
df=df.dropna(how="any")

# Acquire percent number and filter bottom 10 percent
p = np.percentile(df.Market_Cap, 10)

# save as tickerList
tickerList = df[(df.Market_Cap > p)]
# print(tickerList.head(10))

#Technology
Tech = tickerList[tickerList['Industry'].isin(['Computer Manufacturing', 'Computer Software: Prepackaged Software',
                                               'Computer peripheral equipment','Computer Software: Programming Data Processing'
                                               ,'Computer Communications Equipment','Internet and Information Services'])]


Tech = Tech.drop('Industry', axis=1)
# print(Tech.head(10))
# Tech.to_csv('my_dataframe.csv', index=False)

print(type(Tech.Symbol.tolist()))
keyword = Tech.Symbol.tolist()
from GoogleNews import GoogleNews
import pandas as pd

# create a GoogleNews object
googlenews = GoogleNews(lang='en')
data = []
for symbol in keyword:
    all_data = googlenews.search(symbol)
    googlenews.setperiod('1d')
    results = googlenews.result()
# initialize
    for result in results:
        headline = result['title']
        date = result['date']
        data.append([headline, date, symbol])

df = pd.DataFrame(data, columns=['Headline', 'Publish Date','Company'])

# export the dataframe to a CSV file
df.to_csv('news_headlines.csv', index=False)
print(df)