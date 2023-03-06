#! /usr/bin/env python

import requests
import streamlit as st
import pandas as pd

endpoint = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=USD&days=10&interval=hourly'
schema = '{"prices":[[timestamp in UNIX, price], ... ]}' 

st.title('Bitcoin Price')

response = requests.get(endpoint)
data = response.json()

df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

st.line_chart(df, x = 'timestamp', y = 'price')
