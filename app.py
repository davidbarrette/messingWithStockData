import pandas as pd 
from alpha_vantage.timeseries import TimeSeries
from twilio.rest import Client

from twilio_text_auth import *

API_KEY = '4OBRDZAAXWHRRJGV'

ts = TimeSeries(key=API_KEY, output_format='pandas')
data, meta_data = ts.get_daily(symbol='MSFT', outputsize='full')
print(data)

#Texting, will run when some condition I must see is passed
client =  Client(get_acccount_SID(), get_auth_token())

client.messages.create(to="+12242775176", 
                       from_="+12058786233", 
                       body="Hello from Python!")