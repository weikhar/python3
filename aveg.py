# https://github.com/RomelTorres/av_example/blob/master/Alpha%20vantage%20examples.ipynb
API_KEY = "M3CLIFYJLP54DKZA"
#matplotlib inline
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib
import matplotlib.pyplot as plt
import os
from pandas import DataFrame
# Make plots bigger
# matplotlib.rcParams['figure.figsize'] = (20.0, 10.0)

def av1():
    print("\n1) Working with time Series")
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
    # We can describe it
    print(data.describe())
    input("printed time-series data - press Enter to continue...")
    #table
    data['4. close'].plot()
    plt.title('Intraday Times Series for the MSFT stock (1 min)')
    plt.grid()
    plt.show()
    input("\nShown time-series plot 1 - press Enter to continue...")
    #plot of Intraday Time Series for the MSFT stock (1min)
    # Check the meta data given back by the api call.
    print(meta_data)
    input("printed meta_data - press Enter to continue...")

def av2():
    print("\n2) Getting csv data")
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
    
    ts = TimeSeries(key=API_KEY, output_format='csv')
    data_csv,_ = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='compact')
    print(data_csv)
    input("printed data_csv - press Enter to continue...")
    data = data.drop('5. volume',1)
    data.plot()
    plt.title('Intraday Times Series for the MSFT stock (1 min)')
    plt.grid()
    plt.show()
    input("\nShown time-series plot 2 - press Enter to continue...")

def av3():
    #Working with batch quotes
    print("\n3) Working with batch quotes")
    ts = TimeSeries(key=API_KEY, output_format='csv')
    # It is still a TimeSeries call
    ts.output_format='pandas'
    data, meta_data = ts.get_batch_stock_quotes(symbols=('MSFT', 'FB', 'AAPL'))
    data.describe()
    print(data)
    input("\nShown batch data - press Enter to continue...")
    data.head(3)
    print(data)
    input("\nShown batch data with head(3) - press Enter to continue...")

def av4():
    #Working with technical indicators
    print("\n4) Working with technical indicators")
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
    data.describe()
    print(data)
    input("\nShown technical indicators data - press Enter to continue...")
    print(meta_data)
    input("\nShown technical indicators meta_data - press Enter to continue...")
    data.plot()
    plt.title('BBbands indicator for  MSFT stock (60 min)')
    plt.grid()
    plt.show()
    input("\nShown technical indicators plot 3 - press Enter to continue...")

def av5():
    print("\n5) Working with Sector Performance")
    sp = SectorPerformances(key=API_KEY, output_format='pandas')
    data, meta_data = sp.get_sector()
    data.describe()
    print(data)
    input("\nShown sector performance data - press Enter to continue...")
    print(meta_data)
    input("\nShown sector performance meta_data - press Enter to continue...")
    data['Rank A: Real-Time Performance'].plot(kind='bar')
    plt.title('Real Time Performance (%) per Sector')
    plt.tight_layout()
    plt.grid()
    plt.show()
    input("\nShown sector performance plot 4 - press Enter to continue...")

def av6():
    print("\n6) Working with Crypto Currencies")
    cc = CryptoCurrencies(key=API_KEY)
    # get intraday price of bitcoin
    # I changed the internal format of the the class to be our friendly data frame.
    cc.output_format='pandas'
    data, meta_data = cc.get_digital_currency_intraday(symbol='BTC', market='CNY')
    data.describe()
    print(data)
    input("\nprinted data table of intraday bitcoin")
    data.head(5)
    print(data)
    input("\nprinted data table of intraday bitcoin - head(5)")
    data['1b. price (USD)'].plot()
    plt.tight_layout()
    plt.title('Intraday value for bitcoin (BTC)')
    plt.grid()
    plt.show()
    input("\nShown intraday bitcoinvalue plot 4 - press Enter to continue...")

def menu():
    print("\nMenu:")
    print("1) Time Series")
    print("2) CSV data")
    print("3) Batch quotes")
    print("4) Technical indicators")
    print("5) Sector Performance")
    print("6) Crypto Currencies")
    print("99) Exit")
    x = int(input("\nEnter a number  <1..6 | 99>: "))
    if x > 0 and x < 7:
    	options[x]()
    	menu()
    elif x == 99:
    	global done_demo
    	done_demo = 0

#------- start here -------
# map the inputs to the function blocks
options = {1 : av1,
   2 : av2,
   3 : av3,
   4 : av4,
   5 : av5,
   6 : av6,
}
global done_demo 
done_demo = 1
while done_demo:
    menu()

print("\n\nEND")
