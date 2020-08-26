
from src.data_collector import DataCollector    #Collect data to be analized
from src.textNotifications import TextNotifier

dc = DataCollector()
dc.printData()

#Texting, will run when some condition I must see is passed
importantEvent = True
if(importantEvent):
    texter = TextNotifier()
    # texter.sendText()
    