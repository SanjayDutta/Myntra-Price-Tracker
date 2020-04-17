import os
from twilio.rest import Client

class sendWhatsAppsms:
    def __init__(self,message,tpi,tsec,tphone,phone):
        account_sid = tpi #
        auth_token = tsec #tphone:+14155238886
        client = Client(account_sid, auth_token)

        from_whatsapp_number = 'whatsapp:'+str(tphone)
        to_whatsapp_number = 'whatsapp:+91'
        to_whatsapp_number = to_whatsapp_number + phone

        client.messages.create(body=message,
                               from_=from_whatsapp_number,
                               to=to_whatsapp_number)


