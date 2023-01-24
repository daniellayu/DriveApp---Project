import tkinter.messagebox
from tkinter import *

class MyWindow():
    def __init__(self):
        window = Tk()
        window.geometry("300x300")
        window.configure(bg="pink")
        self.fname = Label(window, text="first name", background="yellow")
        self.fname.place(x=50, y=50)
        self.lname = Label(window, text="last name", background="yellow")
        self.lname.place(x=50, y=100)
        self.adress = Label(window, text="adress", background="yellow")
        self.adress.place(x=50, y=150)
        self.phone_number = Label(window, text="phone number", background="yellow")
        self.phone_number.place(x=50, y=200)
        self.et_fname = Entry(window)
        self.et_fname.place(x=150, y=50)
        self.et_lname = Entry(window)
        self.et_lname.place(x=150, y=100)
        self.et_adress = Entry(window)
        self.et_adress.place(x=150, y=150)
        self.et_phone_number = Entry(window)
        self.et_phone_number.place(x=150, y=200)
        self.btn_submit = Button(text="submit", command=self.clickme, background="red")
        self.btn_submit.place(x=125, y=250)
        window.mainloop()


    def clickme(self):
        tkinter.messagebox.showinfo("details", self.et_fname.get() + " " + self.et_lname.get() + " " + self.et_adress.get() + " " + self.et_phone_number.get())


w = MyWindow()

