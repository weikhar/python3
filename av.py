# https://alpha-vantage.readthedocs.io/en/latest/index.html
# pip install alpha_vantage
# pip install pandas
import os
#print("Python3 script:", os.path.basename(__file__))
YOUR_API_KEY = 'M3CLIFYJLP54DKZA'

from pprint import pprint
from alpha_vantage.timeseries import TimeSeries
#from alpha_vantage.timeseries import TimesSeries

print("\nData Frame Structure")
ts = TimeSeries(key=YOUR_API_KEY, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(2))
input("Press Enter for next...")

print("\nPlotting in time series")
import matplotlib.pyplot as plt
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()
input("Press Enter for next...")

print("\nTechnical indicators, eg Bolliger Bands")
from alpha_vantage.techindicators import TechIndicators
#import matplotlib.pyplot as plt
ti = TechIndicators(key=YOUR_API_KEY, output_format='pandas')
data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
data.plot()
plt.title('BBbands indicator for  MSFT stock (60 min)')
plt.show()
input("Press Enter for next...")

print("\nSector Performance")
from alpha_vantage.sectorperformance import SectorPerformances
#import matplotlib.pyplot as plt

sp = SectorPerformances(key=YOUR_API_KEY, output_format='pandas')
data, meta_data = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()
input("Press Enter for next...")

print("\nCrypto-currencies - BTC")
from alpha_vantage.cryptocurrencies import CryptoCurrencies
#import matplotlib.pyplot as plt
cc = CryptoCurrencies(key=YOUR_API_KEY, output_format='pandas')
data, meta_data = cc.get_digital_currency_intraday(symbol='BTC', market='CNY')
data['1b. price (USD)'].plot()
plt.tight_layout()
plt.title('Intraday value for bitcoin (BTC)')
plt.grid()
plt.show()
input("Press Enter for next...")

print("\nForex: BTC - USD")
from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
cc = ForeignExchange(key=YOUR_API_KEY)
# There is no metadata in this call
data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency='USD')
pprint(data)
input("Press Enter for next...")

