import UserInfo
import getURL
import xlwt
from xlwt import Workbook
from xlutils.copy import copy
import xlrd
import openpyxl


class TakeInfo(UserInfo.UserInformation, getURL.DataFetcher):

    def putInfoInExcel(self):
        wb_read = xlrd.open_workbook("example.xls")

        sheet_read = wb_read.sheet_by_index(0)
        last_row = sheet_read.nrows

        wb_write = copy(wb_read)

        sheet_write = wb_write.get_sheet(0)

        sheet_write.write(last_row, 0, self.UserName)
        sheet_write.write(last_row, 1, self.UserId)
        sheet_write.write(last_row, 2, self.UserUrl)
        sheet_write.write(last_row, 3, self.ProductName)
        sheet_write.write(last_row, 4, int(self.ProductPrice))
        sheet_write.write(last_row, 5, 1)
        wb_write.save('example.xls')
        self.success = True

    def __init__(self,obj):
        self.UserName = ""
        self.UserId = 0
        self.UserUrl = ""
        self.ProductName = ""
        self.ProductPrice = 0

        user_obj = UserInfo.UserInformation()

        if user_obj.setUserInfo(obj):
            self.UserName, self.UserId, self.UserUrl, self.ProductName, self.ProductPrice = user_obj.getUserInfo()
            #print(self.UserName, self.UserUrl, self.UserId, self.ProductName, self.ProductPrice)
            self.putInfoInExcel()

        else:
            #print("Data can't be entered")
            self.success = False


    def getSucces(self):
        return self.UserName, self.UserId, self.UserUrl, self.ProductName, self.ProductPrice,self.success
#obj = TakeInfo()

