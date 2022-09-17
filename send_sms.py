# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from latestCrime import *


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

numbers_to_message = ['+16823086376', '+14058758142']
latest_crime = latestCrime() #Get the latest crime
for number in numbers_to_message:
    client.messages.create(
        body='\nALERT!!!\nTHERE IS A CRIME DOWN THE STREET RIGHT NOW!\nGo solve the issue please',
        from_='+19787186138',
        media_url=['https://live.staticflickr.com/7186/6806447086_f2c41dfd13_n.jpg'],
        to=number
    )
#message = client.messages \
#                .create(
#                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                     from_='+19787186138',
#                     to='+16823086376, +14058758142'
#                 )

print(message.sid)

