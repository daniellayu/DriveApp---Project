import tkinter
from tkinter import *

class screenB(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('600x600')
        self.title("Screen B")
        str = StringVar()
        str.set("")
        self.w = Label(self, textvariable=str, background="yellow")
        self.w.place(x=100, y=100)
        self.fname = self.parent.etfname.get()
        self.lname = self.parent.etlname.get()
        str.set("welcome:   " + self.fname + "  " + self.lname)
        Button(self, text="close", background="gray", command=self.close).pack(expand=True)

    def close(self):
        self.parent.deiconify()
        self.destroy()