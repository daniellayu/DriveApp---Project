import tkinter
from tkinter import *
from win1 import screenB

class MyWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x800")
        self.title('Screen A')
        self.fname = Label(self, text="First name:", background="light blue")
        self.fname.place(x=100, y=100)
        self.etfname = Entry(self)
        self.etfname.place(x=200, y=100)
        self.lname = Label(self, text="Last name:", background="light blue")
        self.lname.place(x=100, y=300)
        self.etlname = Entry(self)
        self.etlname.place(x=200, y=300)
        self.btn_submit = Button(self, text="submit", background="yellow", command=self.open_screenB).pack(expand=True)

    def open_screenB(self):
        window = screenB(self)
        window.grab_set()
        self.withdraw()


if __name__ == "__main__":
    app = MyWindow()
    app.mainloop()