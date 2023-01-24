import tkinter
from tkinter import *
from DriveProject.server_d.teacherdb import TeacherDb
from tkinter import messagebox
import threading





class SignUpTeacher(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.teacherDb = TeacherDb()
        self.geometry('400x450')
        self.title('Sign up as teacher')
        Label(self, text="SIGN UP Teacher", background="light blue").place(x=150, y=55)
        Label(self, text="first name", background="light blue").place(x=75, y=100)
        self.entry_fname = Entry(self)
        self.entry_fname.place(x=175, y=100)
        Label(self, text="last name", background="light blue").place(x=75, y=125)
        self.entry_lname = Entry(self)
        self.entry_lname.place(x=175, y=125)
        Label(self, text="email", background="light blue").place(x=75, y=150)
        self.entry_email = Entry(self)
        self.entry_email.place(x=175, y=150)
        Label(self, text="phone number", background="light blue").place(x=75, y=175)
        self.entry_phone = Entry(self)
        self.entry_phone.place(x=175, y=175)
        Label(self, text="ID", background="light blue").place(x=75, y=200)
        self.entry_id = Entry(self)
        self.entry_id.place(x=175, y=200)
        Label(self, text="password", background="light blue").place(x=75, y=225)
        self.entry_password = Entry(self)
        self.entry_password.place(x=175, y=225)
        Label(self, text="experience", background="light blue").place(x=75, y=250)
        self.entry_experience = Entry(self)
        self.entry_experience.place(x=175, y=250)
        Label(self, text="price", background="light blue").place(x=75, y=275)
        self.entry_price = Entry(self)
        self.entry_price.place(x=175, y=275)
        self.btn_signup = Button(self, text="Sign up", background="purple", command=self.sign_up_teacher).place(x=150, y=350)
        self.btn_close = Button(self, text="close", background="red", command=self.close).place(x=150, y=400)

    def sign_up_teacher(self):
        print(self.entry_id.get())
        if (len(self.entry_id.get()) == 0) or (len(self.entry_password.get()) == 0):
            messagebox.showerror("Please write ID and password", "Error")
            return False
        print("sign_up_teacher")
        arr = ["sign_up_teacher", self.entry_fname.get(), self.entry_lname.get(), self.entry_email.get(), self.entry_phone.get(), self.entry_id.get(), self.entry_password.get(), self.entry_experience.get(), self.entry_price.get()]
        str_insert = ",".join(arr)
        print(str_insert)
        self.parent.client_socket.send(str_insert.encode())
        data = self.parent.client_socket.recv(1024).decode()
        print(data)

    def handle_add_user(self):
        self.client_handler = threading.Thread(target=self.sign_up_teacher, args=())
        self.client_handler.daemon = True
        self.client_handler.start()

    def close(self):
        self.parent.deiconify()
        self.destroy()
