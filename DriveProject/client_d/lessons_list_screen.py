import tkinter
from tkinter import *
from tkinter import ttk, messagebox


class LessonsList(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('700x400')
        self.title('Lessons List Screen')
        self.table = ttk.Treeview(self, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show="headings", heigh="7")
        self.table.column("#1", anchor=CENTER, width=100)
        self.table.column("#2", anchor=CENTER, width=100)
        self.table.column("#3", anchor=CENTER, width=100)
        self.table.column("#4", anchor=CENTER, width=100)
        self.table.column("#5", anchor=CENTER, width=100)
        self.table.column("#6", anchor=CENTER, width=100)
        self.table.heading("#1", text="lessonId")
        self.table.heading("#2", text="teacherId")
        self.table.heading("#3", text="studentId")
        self.table.heading("#4", text="date")
        self.table.heading("#5", text="time")
        self.table.heading("#6", text="price")
        self.table.place(x=45, y=100)
        self.listbox()
        self.btn_close = Button(self, text="Close", background="red", command=self.close)
        self.btn_close.place(x=650, y=370)


    def listbox(self):
        arr = ["lessons_list"]
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
            line1 = item.split(",")
            self.table.insert("", 'end', text="1", values=(line1[0], line1[1], line1[2], line1[3], line1[4], line1[5]))


    def close(self):
        self.parent.deiconify()
        self.destroy()