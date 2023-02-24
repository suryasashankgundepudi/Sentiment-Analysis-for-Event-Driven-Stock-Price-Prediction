import pandas as pd
import numpy as np

# read in data and conduct basic data clean and rename columns
df=pd.read_csv(r'nasdaq_screener_1675799625051.csv',usecols=["Symbol","Name",'Country',"Last Sale","Market Cap","Industry"])
df.columns = ["Symbol","Name","Last_Sale","Market_Cap",'Country',"Industry"]
df=df.dropna(how="any")

# Acquire percent number and filter bottom 10 percent
p = np.percentile(df.Market_Cap, 10)

# save as tickerList
tickerList = df[(df.Market_Cap > p)]
# print(tickerList.head(10))

#Technology
Tech = tickerList[tickerList['Industry'].isin([ 'Computer Software: Prepackaged Software',
                                               'Computer Software: Programming Data Processing'
                                               ,'Computer Communications Equipment','Internet and Information Services',
                                               'Retail: Computer Software & Peripheral Equipment'])]
print(Tech.shape)
Tech = Tech[Tech['Country'].isin(['United States'])]
Tech = Tech.drop('Industry', axis=1)
Tech = Tech.drop('Country',axis = 1)
# print(Tech.head(10))
# Tech.to_csv('my_dataframe.csv', index=False)
print(Tech.shape)
print(type(Tech.Name.tolist()))
keyword = Tech.Name.tolist()
# print(Tech.head(10))
# Tech.to_csv('my_dataframe.csv', index=False)

from gnews import GNews
import time
import requests.exceptions

data = []
try:
    googlenews = GNews(language='en', country='US', period='3m')
    for symbol in keyword:
        print('1') # check progress
        time.sleep(3)

        for result in googlenews.get_news(symbol):
            headline = result['title']
            date = result['published date']
            data.append([headline, date, symbol])
    import pandas as pd
    df = pd.DataFrame(data, columns=['Headline', 'Publish Date', 'company'])

    # export the dataframe to a CSV file
    df.to_csv('test.csv', index=False)
    print(df)

except requests.exceptions.RequestException as e:
    print(f"Error acquiring news: {e}")
