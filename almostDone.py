import pandas as pd
import ujson, requests, os
from socrata.authorization import Authorization
from socrata import Socrata
from sodapy import Socrata
import os
from twilio.rest import Client
import time

time2 = '00:00:00'

i=0

for i in range (0,5):
    auth = Authorization(
        "",
        "ay6ucx8w0pkf3wpblrvah7zfq",
        "22m1ry5evkqtlnigmf79s79spk2r7rv04s3ewbwv38gvcjx9lf"
    )

    client = Socrata(
        "www.dallasopendata.com",
        "JEh8Dh72mlqeCbRYUcSq5CVbQ",
        timeout=10
    )

    results = client.get("9fxf-t2tr")

    df_dallaspd = pd.DataFrame.from_records(results)
    df_dallaspd=df_dallaspd.sort_values(by=['date', 'time'], ascending=False)
    incident_report = df_dallaspd.iloc[0]

    #prints the entire dictionary/list
    #print(incident_report)
    #setting up vars to use in the output?

    location1 = incident_report['location']
    division1 = incident_report['division']
    time1 = incident_report['time']
    status1 = incident_report['nature_of_call']
    incidentNumber1 = incident_report['incident_number']
    incidentReport1 = incident_report['block']
    
    

    if time1 != time2:
        text = (f'INCIDENT REPORT ALERT-\nAn incident described as "{status1}" has been reported near {location1}, located in the {division1} division of Dallas.\nThe incident occurred at {time1}.\n\nIncident Number: {incidentNumber1}\tIncident Block # {incidentReport1}') 
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

    print(time1)
    print(time2)
    
    time2 = time1

            
            
    time.sleep(120)
    
