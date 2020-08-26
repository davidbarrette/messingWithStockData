from twilio.rest import Client
from src.twilio_text_auth import *

TWILIO_PHONE_NUMBER = "+12058786233"
MY_PHONE_NUMBER = "+12242775176"

class TextNotifier(object):
    def __init__(self):
        self.client =  Client(get_acccount_SID(), get_auth_token())

    def sendText(self, str = "no message body"):
        self.client.messages.create(to=MY_PHONE_NUMBER, 
                            from_=TWILIO_PHONE_NUMBER, 
                            body=str)