

location1 = 'S Westmoreland Rd'
division1 = 'Southwest'
time1 = '15:10:27'
status1 = '6X - Major Dist (Violence)'
incidentNumber1 = '22-1830016'
incidentReport1 = '7600'


text = (f'INCIDENT REPORT ALERT-\nAn incident described as "{status1}" has been reported near {location1}, located in the {division1} divisionof Dallas.\nThe incident occurred at {time1}.\n\nIncident Number: {incidentNumber1}\tIncident Block # {incidentReport1}') 
# , incident_report('status'), incident_report('incident_number'), incident_report('block'))



# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
#from latestCrime import *


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

numbers_to_message = ['+16823086376', '+14058758142']
for number in numbers_to_message:
    client.messages.create(
        body= text,
        from_='+19787186138',
        to=number
    )
#message = client.messages \
#                .create(
#                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                     from_='+19787186138',
#                     to='+16823086376, +14058758142'
#                 )

# print(message.sid)
