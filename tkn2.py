import tkinter.messagebox
from tkinter import *

class Tkn():
    def __init__(self):
        window = Tk()
        window.geometry("500x300")
        self.rtype = Label(window, text="restaurant type", background="yellow")
        self.rtype.place(x=50, y=50)
        self.num = Label(window, text="num of workers", background="yellow")
        self.num.place(x=50, y=100)
        self.cityid = Label(window, text="city ID", background="yellow")
        self.cityid.place(x=50, y=150)
        self.et_rtype = Entry(window)
        self.et_rtype.place(x=150, y=50)
        self.et_num = Entry(window)
        self.et_num.place(x=150, y=100)
        self.et_cityid = Entry(window)
        self.et_cityid.place(x=150, y=150)
        self.btn_submit = Button(text="submit", command=self.clickme(), background="red")
        self.btn_submit.place(x=125, y=200)
        window.mainloop()

    def clickme(self):
        tkinter.messagebox.showinfo("details", self.et_rtype.get() + " " + self.et_num.get() + " " + self.et_cityid.get())


w = Tkn()