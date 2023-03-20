import pandas as pd
import datetime as dt


ticker = "META"
# read in data and conduct basic data clean and rename columns
df_M = pd.read_csv(r'../data/' +  ticker + '_article_titles.csv')
df_M_S = pd.read_csv(r'../data/' + ticker + '.csv', usecols=["Date", "Open", "Close"])
df_M_S = df_M_S.rename(columns={'Date': 'publish_date'})

df_M['publish_date'] = pd.to_datetime(df_M['publish_date'])
df_M_S['publish_date'] = pd.to_datetime(df_M_S['publish_date'])

# merge datasets
data = (pd.merge(df_M, df_M_S, on='publish_date'))
time_period = dt.timedelta(days=30)

# loop through the dataframe and check for price changes
for i in range(len(data)):
    current_price = data.loc[i, 'Close']
    current_datetime = data.loc[i, 'publish_date']
    next_month_datetime = current_datetime + time_period
    next_month_prices = data[(data['publish_date'] > current_datetime) & (data['publish_date'] <= next_month_datetime)][
        'Close']
    if len(next_month_prices) > 0:
        next_month_price = next_month_prices.iloc[0]
        if next_month_price >= current_price * 1.05:
            data.loc[i, 'price_change'] = 1  # price increased by 5% or more
            if next_month_price >= current_price * 1.1:
                data.loc[i, 'price_change'] = 2
        elif next_month_price <= current_price * 0.95:
            data.loc[i, 'price_change'] = -1  # price decreased by 5% or more
            if next_month_price <= current_price * 0.9:
                data.loc[i, 'price_change'] = -2
        else:
            data.loc[i, 'price_change'] = 0  # price did not change by 5% or more
    else:
        data.loc[i, 'price_change'] = 0  # no next month price available

print(data.head(10))

data = data.drop(['Close', "Open"], axis=1)
data = data.sort_values(by='publish_date', ascending=True)
data.reset_index(drop=True, inplace=True)

data.to_csv("../data/" + ticker + "_price_change.csv", sep=',', encoding='utf-8',
            header=True)

