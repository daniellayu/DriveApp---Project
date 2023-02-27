import tkinter
from tkinter import *
from tkinter import ttk, messagebox


class UpdateDetails(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('300x300')
        self.title('Update Details Screen')
        Label(self, text="first name:").place(x=40, y=75)
        self.entry_fname = Entry(self)
        self.entry_fname.place(x=125, y=75)
        Label(self, text="price:").place(x=40, y=125)
        self.entry_price = Entry(self)
        self.entry_price.place(x=125, y=125)
        Label(self, text="years of experience:").place(x=40, y=175)
        self.entry_experience = Entry(self)
        self.entry_experience.place(x=125, y=175)
        self.btn_update = Button(self, text="update", background="pink", command=self.update).place(x=110, y=225)
        self.btn_close = Button(self, text="close", background="red", command=self.close).place(x=110, y=275)


    def update(self):
        if (len(self.entry_price.get()) == 0) and (len(self.entry_experience.get()) == 0):
            messagebox.showerror("error", "please write your new details")
            return
        arr = ["update_details", self.entry_fname.get(), self.entry_price.get(), self.entry_experience.get()]
        str = ",".join(arr)
        print(str)
        self.parent.parent.parent.client_socket.send(str.encode())
        data = self.parent.parent.parent.client_socket.recv(1024).decode()#recived success or failed
        print(data)
        if data == "success update details":
            messagebox.showinfo("showinfo", "your details have been successfully updated")
        if data == "failed update details":
            messagebox.showerror("error", "try again")


    def close(self):
        self.parent.deiconify()
        self.destroy()
