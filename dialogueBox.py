from tkinter import *
import sys
from tkinter import messagebox


class DialogueBox:

    def __init__(self):
        self.root = Tk(className='mpt- Myntra Price Tracker')
        self.root.geometry("650x200")
        self.root.configure(background='#ecb275')
        myLabel0 = Label(self.root, text="Myntra Price Tracker", font="Bahnschrift 22", padx=10, pady=10, foreground="Red",
                         bg='#ecb275').grid(row=0, column=0)

        myLabel1 = Label(self.root, text="Enter Name", font="Bahnschrift", bg='#ecb275').grid(row=1, column=0)
        self.myEntryLabel1 = Entry(self.root, width=50)
        self.myEntryLabel1.grid(row=1, column=1)

        myLabel2 = Label(self.root, text="Paste URL", font="Bahnschrift", bg='#ecb275').grid(row=2, column=0)
        self.myEntryLabel2 = Entry(self.root, width=50)
        self.myEntryLabel2.grid(row=2, column=1)

        myButton = Button(self.root, text="Submit", command=self.myClick, width=30).grid(row=4, column=1)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        self.UserName = ""
        self.UserUrl = ""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
        sys.exit()


    def myClick(self):
        self.UserName = self.myEntryLabel1.get()
        self.UserUrl = self.myEntryLabel2.get()
        self.root.destroy()
        #print(self.UserUrl)

        #print(self.UserName)

    def getUserNameURL(self):
        #pass
        return self.UserName, self.UserUrl
        #return "ABC","https://www.myntra.com/shirts/highlander/highlander-men-blue--white-slim-fit-checked-casual-shirt/2006852/buy"

#obj = DialogueBox()
