import random
import dialogueBox
import re
import getURL
from tkinter import *

class UserInformation():

    def __init__(self):
        self.UserName = ""
        self.UserURL = ""
        self.UserId = 0

    def checkURL(self):
        #print("In checkURL:",self.UserName, self.UserURL)
        x = re.search("^https://www.myntra.com/.*$", self.UserURL)
        y = re.search("^www.myntra.com/.*$", self.UserURL)
        if x or y:
            return True
        else:
            return False

    def setUserInfo(self,obj):

        self.UserName, self.UserURL = obj.getUserNameURL()
        if UserInformation.checkURL(self):
            self.UserId = self.UserName[0] + self.UserName[1] + self.UserName[2] + str((ord(self.UserName[0])) + (ord(self.UserName[1])) *10 + (ord(self.UserName[2])*100))
            obj = getURL.DataFetcher(self.UserURL)
            valid,self.ProductName, self.ProductPrice = obj.getPrice()
            if valid == 0:
                return False
            else:
                return True
        else:
            return False

    def showUserInfo(self):
        print("Name: ", self.UserName, " Id: ", self.UserId)

    def getUserInfo(self):
        return self.UserName, self.UserId, self.UserURL, self.ProductName, self.ProductPrice



#obj = UserInformation()
#obj.setUserInfo()