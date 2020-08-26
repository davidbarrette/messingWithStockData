import pandas as pd 
from alpha_vantage.timeseries import TimeSeries

API_KEY = '4OBRDZAAXWHRRJGV'
SYMBOL = 'MSFT'

class DataCollector(object):
    def __init__(self):
        ts = TimeSeries(key=API_KEY, output_format='pandas')
        data, meta_data = ts.get_daily(symbol=SYMBOL, outputsize='full')
        self.data = data
        self.meta_data = meta_data
    
    def getData(self):
        return self.data
        
    def printData(self):
        print(self.data)
    
