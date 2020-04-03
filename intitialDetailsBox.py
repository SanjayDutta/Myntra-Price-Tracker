from tkinter import *
import sys
import xlrd
import xlwt
from xlwt import Workbook

from tkinter import messagebox

class initialDetailsBox():

    def __init__(self):
        loc = ("example.xls")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        if sheet.nrows == 1:
            self.activate = 1
        else:
            self.activate = 0

    def takeInfo(self):
        if self.activate == 1:
            self.root = Tk(className='mpt-User Details')
            #self.root.geometry("650x200")
            self.root.configure(background='#ecb275')
            myLabel1 = Label(self.root, text="Enter Name", font="Bahnschrift", bg='#ecb275').grid(row=1, column=0)
            self.myEntryLabel1 = Entry(self.root, width=50)
            self.myEntryLabel1.grid(row=1, column=1)

            myLabel2 = Label(self.root, text="Phone No(+91xxxxxxxxxx)", font="Bahnschrift", bg='#ecb275').grid(row=2, column=0)
            self.myEntryLabel2 = Entry(self.root, width=50)
            self.myEntryLabel2.grid(row=2, column=1)

            myLabel3 = Label(self.root, text="Enter email", font="Bahnschrift", bg='#ecb275').grid(row=3, column=0)
            self.myEntryLabel3 = Entry(self.root, width=50)
            self.myEntryLabel3.grid(row=3, column=1)

            myLabel4 = Label(self.root, text="Enter Twilio Phone Number:", font="Bahnschrift", bg='#ecb275').grid(row=4, column=0)
            self.myEntryLabel4 = Entry(self.root, width=50)
            self.myEntryLabel4.grid(row=4, column=1)

            myLabel5 = Label(self.root, text="Enter Twilio Api Key", font="Bahnschrift", bg='#ecb275').grid(row=5, column=0)
            self.myEntryLabel5 = Entry(self.root, width=50)
            self.myEntryLabel5.grid(row=5, column=1)

            myLabel6 = Label(self.root, text="Enter Twilio Api Secret Key", font="Bahnschrift", bg='#ecb275').grid(row=6, column=0)
            self.myEntryLabel6 = Entry(self.root, width=50)
            self.myEntryLabel6.grid(row=6, column=1)

            myButton = Button(self.root, text="Submit", command=self.myClick, width=30).grid(row=7, column=1)

            #self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.root.mainloop()

    def myClick(self):
        self.UserName = self.myEntryLabel1.get()
        self.PhoneNo = self.myEntryLabel2.get()
        self.email = self.myEntryLabel3.get()
        self.TphoneNo =self.myEntryLabel4.get()
        self.TapiKey =self.myEntryLabel5.get()
        self.TapiSec =self.myEntryLabel6.get()
        print("Username: ",self.UserName,
              "\nPhone No: ",self.PhoneNo,
              "\nEmail: ",self.email,
              "\nt Phone: ",self.TphoneNo,
              "\nt api: ",self.TapiKey,
              "\nt sec: ",self.TapiSec)

        self.root.destroy()

    def getInfo(self):
        if self.activate == 1:
            wb = Workbook()
            sheet1 = wb.add_sheet('Sheet 1')
            sheet1.write(0, 0, self.email)
            sheet1.write(1, 0, self.TphoneNo)
            sheet1.write(2, 0, self.TapiKey)
            sheet1.write(3, 0, self.TapiSec)
            sheet1.write(4, 0, self.PhoneNo)
            wb.save('user.xls')
        else:
            loc = ("user.xls")
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            self.email = sheet.cell_value(0, 0)
            self.TphoneNo = sheet.cell_value(1, 0)
            self.TapiKey = sheet.cell_value(2, 0)
            self.TapiSec = sheet.cell_value(3, 0)
            self.PhoneNo = sheet.cell_value(4, 0)

        return self.email,self.TphoneNo, self.TapiKey,self.TapiSec,self.PhoneNo
