import threading
import tkinter
from tkinter import *
from add_users import Register
from login import Login
import socket
from tkinter import ttk, messagebox
from users import *


class App(tkinter.Tk):
    def __init__(self):
        self.userDb=User()
        super().__init__()
        self.geometry('300x300')
        self.title('Main Window')
        self.btn_register = Button(self, text='Register', command=self.open_register)
        self.btn_register.place(x=50, y=50)
        self.handle_thread_socket()
        Label(self, text="Email: ", background="light blue").place(x=50, y=100)
        self.entry_email = Entry(self)
        self.entry_email.place(x=120, y=100)
        Label(self, text="Password: ", background="light blue").place(x=50, y=150)
        self.entry_password = Entry(self)
        self.entry_password.place(x=120, y=150)
        self.btn_login = Button(self, text='Login', command=self.login_user)
        self.btn_login.place(x=120, y=200)
        self.label_login = Label(self, textvariable=str, background="light blue")
        self.label_login.place(x=120, y=250)
        self.str = StringVar()
        self.str.set("")
        Label(self, textvariable=self.str, background="pink").place(x=50, y=250)

    def open_register(self):
        window = Register(self)
        window.grab_set()
        self.withdraw()

    def open_login(self):
        window = Login(self)
        window.grab_set()
        self.withdraw()

    def handle_thread_socket(self):
        client_handler = threading.Thread(target=self.create_socket, args=())
        client_handler.daemon = True
        client_handler.start()

    def create_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 1802))
        data = self.client_socket.recv(1024).decode()
        print("data"+data)
        print("hi", self.client_socket)

    def login_user(self):
        if len(self.entry_email.get()) == 0 and len(self.entry_password.get()) == 0:
            messagebox.showerror("please write email and password", "Error")
            return
        print("login")

        if self.userDb.is_exist(self.entry_email.get(),self.entry_password.get())==False:
            message = "Please register"
            self.str.set(message)
            print(self.str.get())
        else:
            message2="Welcome,You are logged in"
            self.str.set(message2)
            print(self.str.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()
