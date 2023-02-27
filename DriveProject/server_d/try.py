import sqlite3
import tkinter

from tkinter import *
from tkinter import ttk


# conn = sqlite3.connect('database.db')
# c = conn.cursor()
#
# c.execute("SELECT * FROM StudentDb")
# data = c.fetchall()
# conn.close()
#
# print(str(data))

class View(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x400')
        self.table = ttk.Treeview(self, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show="headings", heigh="7")
        self.table.column("#1", anchor=CENTER, width=100)
        self.table.column("#2", anchor=CENTER, width=100)
        self.table.column("#3", anchor=CENTER, width=100)
        self.table.column("#4", anchor=CENTER, width=100)
        self.table.column("#5", anchor=CENTER, width=100)
        self.table.column("#6", anchor=CENTER, width=100)
        self.table.heading("#1", text="studentId")
        self.table.heading("#2", text="first name")
        self.table.heading("#3", text="last name")
        self.table.heading("#4", text="email")
        self.table.heading("#5", text="phone number")
        self.table.heading("#6", text="id")
        self.table.insert()
        self.table.place(x=45, y=100)

if __name__ == "__main__":
    v = View()
    v.mainloop()

