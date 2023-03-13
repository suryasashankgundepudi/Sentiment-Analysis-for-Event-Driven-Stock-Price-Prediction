import pandas as pd
import numpy as np
import datetime as dt

# read in data and conduct basic data clean and rename columns
df_M=pd.read_csv(r'META_article_sentiments.csv')
df_M_S = pd.read_csv(r'META.csv',usecols=["Date","Open","Close"])
df_M_S = df_M_S.rename(columns={'Date': 'publish_date'})

df_M['publish_date'] = pd.to_datetime(df_M['publish_date'])
df_M_S['publish_date'] = pd.to_datetime(df_M_S['publish_date'])

# merge datasets
META = (pd.merge(df_M, df_M_S, on='publish_date'))
time_period = dt.timedelta(days=30)

# loop through the dataframe and check for price changes
for i in range(len(META)):
    current_price = META.loc[i, 'Close']
    current_datetime = META.loc[i, 'publish_date']
    next_month_datetime = current_datetime + time_period
    next_month_prices = META[(META['publish_date'] > current_datetime) & (META['publish_date'] <= next_month_datetime)]['Close']
    if len(next_month_prices) > 0:
        next_month_price = next_month_prices.iloc[0]
        if next_month_price >= current_price * 1.05:
            META.loc[i, 'price_change'] = 1  # price increased by 5% or more
            if next_month_price >= current_price * 1.1:
                META.loc[i, 'price_change'] = 2
        elif next_month_price <= current_price * 0.95:
            META.loc[i, 'price_change'] = -1  # price decreased by 5% or more
            if next_month_price <= current_price * 0.9:
                META.loc[i, 'price_change'] = -2
        else:
            META.loc[i, 'price_change'] = 0  # price did not change by 5% or more
    else:
        META.loc[i, 'price_change'] = 0  # no next month price available

print(META.head(10))

META = META.drop(['Close',"Open"], axis=1)
META = META.sort_values(by='publish_date', ascending=True)
META.reset_index(drop=True, inplace=True)

META.to_csv("META_NEWS.csv", sep=',', encoding='utf-8',
                          header=True)

print(META.columns)
