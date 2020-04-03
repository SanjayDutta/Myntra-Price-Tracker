import os
from twilio.rest import Client

class sendWhatsAppsms:
    def __init__(self,message,tpi,tsec,tphone,phone):
        account_sid = tpi #AC86c526e3d3b6c8b9885d4d818cbf12e9
        auth_token = tsec #c2a18c1c07e2e6a170b4b22f825f0f31 #tphone:+14155238886
        client = Client(account_sid, auth_token)

        from_whatsapp_number = 'whatsapp:'+tphone
        to_whatsapp_number = 'whatsapp:+91'
        to_whatsapp_number = to_whatsapp_number + phone

        client.messages.create(body=message,
                               from_=from_whatsapp_number,
                               to=to_whatsapp_number)


