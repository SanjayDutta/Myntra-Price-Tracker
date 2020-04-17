import requests
import json

class sendSMS:


    def __init__(self,email,phoneNo,api_key,api_sec):
        self.URL = 'https://www.sms4india.com/api/v1/sendCampaign'
        self.api_key = api_key
        self.api_sec = api_sec
        self.phoneNo = phoneNo
        self.senderId = email
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