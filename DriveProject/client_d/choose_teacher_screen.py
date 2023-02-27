import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import threading


class ChooseTeacher(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        print(self.parent.parent.parent.client_socket)
        self.geometry('800x400')
        self.title('Choose Teacher Screen')
        self.table = ttk.Treeview(self, columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show="headings", heigh="7")
        self.table.column("#1", anchor=CENTER, width=70)
        self.table.column("#2", anchor=CENTER, width=100)
        self.table.column("#3", anchor=CENTER, width=100)
        self.table.column("#4", anchor=CENTER, width=100)
        self.table.column("#5", anchor=CENTER, width=100)
        self.table.column("#6", anchor=CENTER, width=70)
        self.table.column("#7", anchor=CENTER, width=70)
        #self.table.column("#8", anchor=CENTER, width=70)
        self.table.heading("#1", text="teacher id")
        self.table.heading("#2", text="first name")
        self.table.heading("#3", text="last name")
        self.table.heading("#4", text="email")
        self.table.heading("#5", text="phone number")
        self.table.heading("#6", text="experience")
        self.table.heading("#7", text="price")
        #self.table.heading("#8", text="select")
        self.table.bind('<Button-1>', self.selectItem)
        self.table.place(x=45, y=100)
        self.listbox()
        self.btn_close = Button(self, text="Close", background="red", command=self.close)
        self.btn_close.place(x=750, y=370)

    def selectItem(self, event):
        curItem = self.table.focus()
        print(curItem)
        print(self.table.item(curItem)['values'])
        messagebox.showinfo("showinfo", "you signed to "+self.table.item(curItem)['values'][1])
        self.close()
        #teacher_id = self.table.item(curItem)['values'][0]
        #print("Teacher ID:", teacher_id)

    def listbox(self):
        arr = ["teachers_list"]
        str = ",".join(arr)
        print(str)
        self.parent.parent.parent.client_socket.send(str.encode())
        data = self.parent.parent.parent.client_socket.recv(1024).decode()
        print(data)
        arr_data = data.split("-")
        print(arr_data)
        line1 = arr_data[0].split(",")
        print(line1)
        for item in arr_data:
            #self.b = Button(self, text="select", background="red", command=self.select_teacher)
            line1 = item.split(",")
            self.table.insert("", 'end', text="1", values=(line1[0], line1[1], line1[2], line1[3], line1[4], line1[5], line1[6]))


    def close(self):
        self.parent.deiconify()
        self.destroy()

