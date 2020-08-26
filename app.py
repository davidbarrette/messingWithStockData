import pandas as pd 
from alpha_vantage.timeseries import TimeSeries

API_KEY = '4OBRDZAAXWHRRJGV'

ts = TimeSeries(key=API_KEY, output_format='pandas')
data, meta_data = ts.get_daily(symbol='MSFT', outputsize='full')
print(data)