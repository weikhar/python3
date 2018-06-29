import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import numpy as np
import datetime
import matplotlib.pyplot as plt

from pandas_datareader import data as pdr
import quandl 

gSTART_DATE = "1980-01-01"
gTODAY_DATE = datetime.date.today()
gSTART_YYYY = 1980
gSTART_MM   = 1
gSTART_DD   = 1

#from pandas_datareader import data as pdr
#import fix_yahoo_finance

def get(tickers, startdate, enddate):
    def data(ticker):
        #return (pdr.get_data_yahoo(ticker, start=startdate, end=enddate))
        return (quandl.get(ticker, start=startdate, end=enddate))
    datas = map (data, tickers)
    return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))

tickers = ['WIKI/AAPL', 'WIKI/MSFT', 'WIKI/IBM', 'WIKI/GOOG']
all_data = get(tickers, datetime.datetime(gSTART_YYYY, gSTART_MM, gSTART_DD), gTODAY_DATE)

aapl = quandl.get("WIKI/AAPL", start_date=gSTART_DATE, end_date=gTODAY_DATE)


#----Ordinary Least-Squares Regression (OLS)
# Import the `api` model of `statsmodels` under alias `sm`
import statsmodels.api as sm
from pandas import tseries
from pandas.core import datetools

# Isolate the adjusted closing price
all_adj_close = all_data[['Adj. Close']]
# Calculate the returns 
all_returns = np.log(all_adj_close / all_adj_close.shift(1))
# Isolate the AAPL returns 
aapl_returns = all_returns.iloc[all_returns.index.get_level_values('Ticker') == 'WIKI/AAPL']
aapl_returns.index = aapl_returns.index.droplevel('Ticker')
# Isolate the MSFT returns
msft_returns = all_returns.iloc[all_returns.index.get_level_values('Ticker') == 'WIKI/MSFT']
msft_returns.index = msft_returns.index.droplevel('Ticker')
# Build up a new DataFrame with AAPL and MSFT returns
return_data = pd.concat([aapl_returns, msft_returns], axis=1)[1:]
return_data.columns = ['WIKI/AAPL', 'WIKI/MSFT']
# Add a constant 
X = sm.add_constant(return_data['WIKI/AAPL'])
# Construct the model (OLS = Ordinary Least Squares)
print("\n===OLS #1===\n", return_data['WIKI/AAPL'])
print("\n===OLS #2===\n", X)
input("\nOLS input printed, press Enter to continue..\n")
model = sm.OLS(return_data['WIKI/AAPL'],X).fit()
# Print the summary
print(model.summary())

#plt.plot(return_data['AAPL'], return_data['MSFT'], 'r.')
plt.plot(return_data['WIKI/AAPL'], return_data['WIKI/MSFT'], 'r.')

ax = plt.axis()
x = np.linspace(ax[0], ax[1] + 0.01)

plt.plot(x, model.params[0] + model.params[1] * x, 'b', lw=2)
plt.grid(True)
plt.axis('tight')
plt.xlabel('Apple Returns')
plt.ylabel('Microsoft returns')
plt.title('Ordinary Least-Squares Regression (OLS) - 1')
plt.show()

plt.title('Ordinary Least-Squares Regression (OLS) -2')
#return_data['MSFT'].rolling(window=252).corr(return_data['AAPL']).plot()
return_data['WIKI/MSFT'].rolling(window=252).corr(return_data['WIKI/AAPL']).plot()
plt.show()





#---- Building A Trading Strategy With Python
# Initialize the short and long windows
short_window = 40
long_window = 100
# Initialize the `signals` DataFrame with the `signal` column
signals = pd.DataFrame(index=aapl.index)
signals['signal'] = 0.0
# Create short simple moving average over the short window
signals['short_mavg'] = aapl['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
# Create long simple moving average over the long window
signals['long_mavg'] = aapl['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   
# Generate trading orders
signals['positions'] = signals['signal'].diff()
# Initialize the plot figure
fig = plt.figure()
# Add a subplot and label for y-axis
ax1 = fig.add_subplot(111,  ylabel='Price in $')
# Plot the closing price
aapl['Close'].plot(ax=ax1, color='r', lw=2.)
# Plot the short and long moving averages
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)
# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m')
# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k')
plt.title('Signalling')
# Show the plot
plt.show()



#----Backtesting A Strategy
#----Implementation Of A Simple Backtester With Pandas
# Set the initial capital# Set th 
initial_capital= float(100000.0)
# Create a DataFrame `positions`
positions = pd.DataFrame(index=signals.index).fillna(0.0)
# Buy a 100 shares
positions['AAPL'] = 100*signals['signal']   
# Initialize the portfolio with value owned   
portfolio = positions.multiply(aapl['Adj. Close'], axis=0)
# Store the difference in shares owned 
pos_diff = positions.diff()
# Add `holdings` to portfolio
portfolio['holdings'] = (positions.multiply(aapl['Adj. Close'], axis=0)).sum(axis=1)
# Add `cash` to portfolio
portfolio['cash'] = initial_capital - (pos_diff.multiply(aapl['Adj. Close'], axis=0)).sum(axis=1).cumsum()   
# Add `total` to portfolio
portfolio['total'] = portfolio['cash'] + portfolio['holdings']
# Add `returns` to portfolio
portfolio['returns'] = portfolio['total'].pct_change()

fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Portfolio value in $')

# Plot the equity curve in dollars
portfolio['total'].plot(ax=ax1, lw=2.)
# Plot the "buy" trades against the equity curve
ax1.plot(portfolio.loc[signals.positions == 1.0].index, 
         portfolio.total[signals.positions == 1.0],
         '^', markersize=10, color='m')
# Plot the "sell" trades against the equity curve
ax1.plot(portfolio.loc[signals.positions == -1.0].index, 
         portfolio.total[signals.positions == -1.0],
         'v', markersize=10, color='k')
plt.title('Backtesting')
# Show the plot
plt.show()



#----Evaluating Moving Average Crossover Strategy
#----Sharpe Ratio
# Isolate the returns of your strategy
returns = portfolio['returns']
# annualized Sharpe ratio
sharpe_ratio = np.sqrt(252) * (returns.mean() / returns.std())
# Print the Sharpe ratio
print("\nSharpe Ratio : ", sharpe_ratio)



#----Maximum Drawdown
# Define a trailing 252 trading day window
window = 252
# Calculate the max drawdown in the past window days for each day
rolling_max = aapl['Adj. Close'].rolling(window, min_periods=1).max()
daily_drawdown = aapl['Adj. Close']/rolling_max - 1.0
# Calculate the minimum (negative) daily drawdown
max_daily_drawdown = daily_drawdown.rolling(window, min_periods=1).min()
# Plot the results
daily_drawdown.plot()
max_daily_drawdown.plot()
plt.title('Maximum Drawdown')
# Show the plot
plt.show()


#----Compound Annual Growth Rate (CAGR)
# Get the number of days in `aapl`
days = (aapl.index[-1] - aapl.index[0]).days
# Calculate the CAGR 
cagr = ((((aapl['Adj. Close'][-1]) / aapl['Adj. Close'][1])) ** (365.0/days)) - 1
# Print CAGR
print("\nCompound Annual Growth Rate (CAGR) : ", cagr)


print("\n\n End")