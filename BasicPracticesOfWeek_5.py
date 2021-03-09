# All about APIs Application Program Interface

import pandas as pd
import matplotlib.pyplot as plt
from pygments.lexers import go

dict = {'a':[11,22,33],'b':[12,22,32]}
df = pd.DataFrame(dict)

print(df.head())
print()
print(df.mean(),'\n')

# REST APIs = Representational State Transfer APIs

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

bitcoinData = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd',days=30)
print(bitcoinData)

data = pd.DataFrame(bitcoinData, columns=['TimeStamp', 'Price'])
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')
candlestick_data = data.groupby(data.Date.dt.date).agg({'Price':['min', 'max', 'first', 'last']})

fig = go.Figure(data=[go.Candlestick(x=candlestick_data.index, open = candlestick_data['Price']['first'],
                      high=candlestick_data['Price']['max'],
                      low=candlestick_data['Price']['min'],
                      close=candlestick_data['Price']['last'])
                      ])

fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title='Date', yaxis_title='Price (USD $)', title='Bitcoin Candlestick Chart Over Past 30 Days')
plt.plot(fig, filename = 'bitcoin_candlestick_graph.html')


