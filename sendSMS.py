import requests
import json

class sendSMS:


    def __init__(self):
        self.URL = 'https://www.sms4india.com/api/v1/sendCampaign'
        self.api_key = "EVNM3A8JC3AK6WVM6N8C9MOPQ796LP6P"
        self.api_sec = "127HQSKNNQXE9QYV"
        self.phoneNo = "9831898777"
        self.senderId = "sanjay02081998@gmail.com"
        self.useType = "stage"

    def sendPostRequest(self,textMessage):
        req_params = {
        'apikey':self.api_key,
        'secret':self.api_sec,
        'usetype':self.useType,
        'phone': self.phoneNo,
        'message':textMessage,
       'senderid':self.senderId
        }
        return requests.post(self.URL, req_params)

#object = sendSMS()
#response = object.sendPostRequest("We have your Number. You are going down")
#print(response)