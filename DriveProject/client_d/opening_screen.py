import socket
import threading
import tkinter
from tkinter import *
from sign_in_screen import SignInScreen
from sign_up_as_teacher import SignUpTeacher
from sign_up_as_student import SignupStudent
from PIL import ImageTk, Image


class OpeningScreen(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x550')
        self.title('Opening Screen')
        #self.is_sign_in = False

        self.img = Image.open('C://Users//danie//PycharmProjects//pythonProject//wheel.png')
        self.size = self.img.resize((500, 550), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(self.size)
        self.label_image = Label(self, image=self.image).place(x=0, y=0)

        self.handle_thread_socket()
        self.btn_sign_in = Button(self, text='Sign in', background="light blue", command=self.open_sign_in)
        self.btn_sign_in.place(x=200, y=200)
        self.btn_sign_up_teacher = Button(self, text='Sign up as teacher', background="light blue", command=self.open_sign_up_as_teacher)
        self.btn_sign_up_teacher.place(x=200, y=250)
        self.btn_sign_up_student = Button(self, text='Sign up as student', background="light blue", command=self.open_sign_up_as_student)
        self.btn_sign_up_student.place(x=200, y=300)
        self.btn_exit = Button(self, text="exit", background="red", command=self.exit)
        self.btn_exit.place(x=225., y=350)

    def open_sign_in(self):
        window = SignInScreen(self)
        window.grab_set()
        self.withdraw()

    def open_sign_up_as_teacher(self):
        window = SignUpTeacher(self)
        window.grab_set()
        self.withdraw()

    def open_sign_up_as_student(self):
        window = SignupStudent(self)
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


    def exit(self):
        self.destroy()



if __name__ == "__main__":
    o = OpeningScreen()
    o.mainloop()
