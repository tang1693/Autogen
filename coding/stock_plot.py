# filename: stock_plot.py

import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import os

# current date
now = datetime.datetime.now()

# start & end date for YTD
start_date = datetime.datetime(now.year, 1, 1)
end_date = now.strftime('%Y-%m-%d')

# download stock data
nvda = yf.download('NVDA', start=start_date, end=end_date)["Close"]
tsla = yf.download('TSLA', start=start_date, end=end_date)["Close"]
aapl = yf.download('AAPL', start=start_date, end=end_date)["Close"]

# plot the data
plt.figure(figsize=(14,7))
plt.plot(nvda, label='NVDA')
plt.plot(tsla, label='TESLA')
plt.plot(aapl, label='Apple')
plt.title('NVDA vs TESLA vs Apple Stock Price YTD')
plt.xlabel('Date')
plt.ylabel('Price (Close)')
plt.legend(loc='upper left')
plt.grid(True)

# save the figure to the 'Figures' folder as 'stock_prices.png'
os.makedirs('Figures', exist_ok=True)
plt.savefig('Figures/stock_prices.png')