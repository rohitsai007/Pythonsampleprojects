# -*- coding: utf-8 -*-
"""tradingalgorithm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h9liCxIV1-OuaY2wtdHj1t8-oVZW0MLZ
"""

# Import the libraries
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# Load the files
from google.colab import files
uploaded = files.upload()

AAPL = pd.read_csv('AAPL.csv')

AAPL

plt.figure(figsize=(12.5, 4.5))
plt.plot(AAPL['Adj Close'], label = 'AAPL')
plt.title('Apple Adj close price')
plt.xlabel('March 2006 - May 2020')
plt.ylabel('Adj close price US($)')
plt.savefig('Appleadjcloseprice.png')

SMA12 = pd.DataFrame()
SMA12['Adj Close Price'] = AAPL['Adj Close'].rolling(window=12).mean()
SMA12

SMA36 = pd.DataFrame()
SMA36['Adj Close Price'] = AAPL['Adj Close'].rolling(window=36).mean()
SMA36

plt.figure(figsize=(12.5, 4.5))
plt.plot(AAPL['Adj Close'], label = 'AAPL')
plt.plot(SMA12['Adj Close Price'], label = 'SMA12')
plt.plot(SMA36['Adj Close Price'], label = 'SMA36')
plt.title('Apple Adj close price History')
plt.xlabel('March 2006 - May 2020')
plt.ylabel('Adj close price US($)')
plt.legend(loc='upper left')
plt.savefig('Appleadjclosepricehistory.png')

AAPL

AAPL['Year'] = AAPL['Date'].str[0:4]
AAPL

Year_mean = AAPL.groupby('Year').mean()
Year_mean

yearly = range(2006, 2021)

plt.bar(yearly, Year_mean['High'])
plt.xlabel('Yearly High')
plt.ylabel('High price on year')