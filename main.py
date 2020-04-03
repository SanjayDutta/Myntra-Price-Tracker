import getURL
import UserInfo
import time
import xlwt
from sendWhatsAppsms import sendWhatsAppsms
from xlwt import Workbook
from xlutils.copy import copy
import xlrd
import openpyxl
import dialogueBox
import TakeInfo
from tkinter import *
from threading import *
from getURL import DataFetcher
from sendSMS import sendSMS
from PCNotification import PCN
from intitialDetailsBox import initialDetailsBox

def main():

        class MainBoxClass(Thread):

            def TryAgain(self):
                self.again = True
                self.root1.destroy()

            def ExitProg(self):
                self.again = False
                self.root1.destroy()

            def ifSuccess(self):
                self.root1 = Tk()
                SuccessLabel = Label(self.root1, text="Product Added Successfully, will be tracked",
                                     font="Bahnschrift 22").grid(row=0, column=0)
                UserNameLabel = Label(self.root1, text="User Name: " + self.UserName, font="Bahnschrift 15").grid(row=1, column=0)
                UserIdLabel = Label(self.root1, text="User ID: " + self.UserId, font="Bahnschrift 15").grid(row=2, column=0)
                ProductNameLabel = Label(self.root1, text="Product Name: " + self.ProductName, font="Bahnschrift 15").grid(row=3,
                                                                                                                column=0)
                ProductPriceLabel = Label(self.root1, text="Product Price: " + self.ProductPrice, font="Bahnschrift 15").grid(
                    row=4, column=0)
                myButton1 = Button(self.root1, text="Track More", command=self.TryAgain, width=20).grid(row=5, column=1)
                myButton2 = Button(self.root1, text="Quit", command=self.ExitProg, width=20).grid(row=5, column=2)
                self.root1.mainloop()

            def ifFailure(self):
                self.root1 = Tk()
                ErrorMessage = Label(self.root1, text="URL/Product doesn't exists. Check URL.", font="Bahnschrift 15").grid(
                    row=0, column=0)
                myButton1 = Button(self.root1, text="Try Again", command=self.TryAgain, width=20).grid(row=3, column=1)
                myButton2 = Button(self.root1, text="Exit", command=self.ExitProg, width=20).grid(row=3, column=2)
                self.root1.mainloop()



            def __init__(self):
                 Thread.__init__(self)
                 thread1 = Thread(target=self.MainFunction)
                 thread1.start()
                 #thread1.join()

            def MainFunction(self):
                self.again = True

                while (self.again):

                    obj = dialogueBox.DialogueBox()

                    obj2 = TakeInfo.TakeInfo(obj)
                    self.UserName, self.UserId, self.UserUrl, self.ProductName, self.ProductPrice, self.success = obj2.getSucces()

                    if self.success:
                        MainBoxClass.ifSuccess(self)

                    else:
                        MainBoxClass.ifFailure(self)

        class MainTrackClass(Thread):
            def __init__(self,email,tphone,tapi,tsec,phone):
                self.email = email
                self.tphone = tphone
                self.tapi = tapi
                self.tsec = tsec
                self.phone = phone
                Thread.__init__(self)
                thread2=Thread(target=self.sequencer())
                thread2.start()

            def sequencer(self):
                self.displayName()
                self.trackerService()

            def writeDown(self, rowNum,newProductPrice):
                wbTwo_read = xlrd.open_workbook("example.xls")
                sheet_read = wbTwo_read.sheet_by_index(0)
                last_row = sheet_read.nrows
                wb_write = copy(wbTwo_read)
                sheet_write = wb_write.get_sheet(0)
                sheet_write.write(rowNum, 4, newProductPrice)
                wb_write.save('example.xls')


            def trackerService(self):
                #open excel and find the url and price
                count =0
                while True:
                    print("count:",count)
                    loc = ("example.xls")
                    wb = xlrd.open_workbook(loc)
                    sheet = wb.sheet_by_index(0)
                    i=1
                    time.sleep(5)
                    while i<sheet.nrows and sheet.nrows>1:
                        print("ROWS: ",sheet.nrows)
                        #time.sleep(5)
                        productUrl = sheet.cell_value(i, 2)
                        productPrice = sheet.cell_value(i, 4)
                        #print(productPrice,productUrl)
                        obj = DataFetcher(productUrl)
                        success, ProductName , NewProductPrice = obj.getPrice()
                        print("success: ",success)
                        if success == 1:
                            if int(NewProductPrice) < productPrice:
                                message = "Price went down for: " + ProductName + "\n"
                                message = message + "Old Price: " + str(productPrice) + "\n"
                                message = message + "*New Price: " + NewProductPrice + "*"
                                self.writeDown(i,int(NewProductPrice))
                                obj = sendWhatsAppsms(message,self.tapi,self.tsec,self.tphone,self.phone)  #whatsApp notification
                                obj2 = sendSMS().sendPostRequest(message) #SMS notification
                                obj3 = PCN("Myntra Price Detector",message)

                            elif int(NewProductPrice) > productPrice:
                                print("Price went up for: ",ProductName)
                                self.writeDown(i,int(NewProductPrice))

                            else:
                                print("No change in Price ",ProductName)
                            i = i + 1
                        else:
                            print("Request Failed. Trying Again")
                    count += 1




                #request url and get price
                #compare the urlPrice and ExcelPrice
                #if change send notification, else nothing
                #go to next line in excel



            def displayName(self):
                print("\n\n")
                print("      / /\ \            / /\ \              |‾‾‾‾‾‾‾‾\      |==================|      ")
                print("     / /  \ \          / /  \ \             | |‾‾‾‾‾\ \             | |                ")
                print("    / /    \ \        / /    \ \            | |     | |             | |               ")
                print("   / /      \ \      / /      \ \           | |_____/ /             | |               ")
                print("  / /        \ \    / /        \ \          |  ______/              | |               ")
                print(" / /          \ \  / /          \ \         | |                     | |               ")
                print("/ /            \ \/ /            \ \yntra   | | rice                | | racker        ")
                print(self.email,self.tphone,self.tapi,self.tsec,self.phone )




        #write code from here

        initialBox = initialDetailsBox()
        initialBox.takeInfo()
        email, tphone, tapi, tsec, phone = initialBox.getInfo()


        objectBox = MainBoxClass()
        objectTrack = MainTrackClass(email, tphone, tapi, tsec, phone)

        objectBox.start()
        objectTrack.start()


        objectBox.join()
        objectTrack.join()

if __name__ == '__main__':
    main()