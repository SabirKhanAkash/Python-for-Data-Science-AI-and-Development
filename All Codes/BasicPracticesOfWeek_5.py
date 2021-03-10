# All about APIs Application Program Interface

import pandas as pd
import matplotlib.pyplot as plt
from pygments.lexers import go
import plotly.graph_objects as go

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
# plt.plot(fig, filename = 'bitcoin_candlestick_graph.html')



# from ibm_watson import SpeechToTextV1
#
# url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/001e25b2-526f-4a45-90ec-0d8cad74df70"
# iam_apikey_s2t = "6HdDB1ErYGswPdVHRes99MzeX50se4vxB6k5l6HeEAM2"
# s2t = SpeechToTextV1(iam_apikey=iam_apikey_s2t, url = url_s2t)
#
# filename = 'audio-file.flac'
#
# with open(filename, mode="rb") as flac:
#     response = s2t.recognize(audio=flac, content=flac, content_type='audio/flac')
#
# print(response.result)
# recognized_text = response.result['result'[0]["alternatives"][0]["transcript"]]
# print()
# print(recognized_text)
#
#
# from ibm_watson import LanguageTranslatorV3
# url_lt = 'https://gateway.watsonplatform/net/language-translator/api'
# apikey_lt = 'f5sAznhrKQyvBFFaZbtF60m5tzLbqWhyALQawBg5TjRI'
# version_lt = '2018-05-01'
# language_translator = LanguageTranslatorV3(iam_apikey=apikey_lt, url=url_lt, version=version_lt)
# language_translator.list_identifiable_language().get_result()
#
# recognized_text = 'hello this is python'
# translation_response = language_translator.translate(text=recognized_text, model_id='en-es')
# translation = translation_response.get_result()
#
# translation_new = language_translator.translate(text=spanish_translation, model_id='es-en').get_result()
# translation_eng = translation_new['translations'][0]['translation']
# print(translation_eng)


# SpeechToText API
# 6HdDB1ErYGswPdVHRes99MzeX50se4vxB6k5l6HeEAM2
# https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/001e25b2-526f-4a45-90ec-0d8cad74df70


# Languagetranslator API
# H2ovmASp90KH5-FloxVhe8wrj_F3fe786Je7n4dy6l4i
# https://api.us-south.language-translator.watson.cloud.ibm.com/instances/6fb65312-4dea-47f9-a5c9-5f84d3f45a85


#All about REST APIs and HTTP Requests

import requests
url = 'https://www.ibm.com/'
r = requests.get(url)
print(r.status_code,"\n")
print(r.request.headers,"\n")
print(r.request.body,"\n")
print(r.headers,"\n")

header = r.headers

print(header['date'],"\n")
print(header['content-Type'],"\n")
print(r.encoding,"\n")
print(r.text[0:100],"\n")

# http://httbin.org/get?Name=Akash&ID=1603108

url_get = 'http://httpbin.org/get'
payload = {"name":"Akash","ID":"1603108"}
r = requests.get(url_get,params=payload)
print(r.url,"\n")
print(r.request.body,"\n")
print(r.status_code,"\n")
print(r.text,"\n")
print(r.json(),"\n")

url_post = "http://httpbin.org/post"
payload = {"name":"Akash","ID":"1603108"}
r_post = requests.post(url_post,data=payload)

print("POST request URL: ",r_post.url,"\n")
print("GET request URL: ",r.url,"\n")

print("POST request body: ",r_post.request.body,"\n")
print("GET request body: ",r.request.body,"\n")

print(r_post.json()['form'])
