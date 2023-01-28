import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from students_list_screen import StudentsList
from lessons_list_screen import LessonsList
from update_details_screen import UpdateDetails
import threading


class MenuTeacher(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('400x400')
        self.title('Menu Teacher Screen')
        Label(self, text="Welcome teacher", bg="azure3").place(x=100, y=100)
        self.btn1 = Button(self, text="student's list", bg="light green", command=self.open_students_list)
        self.btn2 = Button(self, text="lessons", bg="light green", command=self.open_lessons_list)
        self.btn3 = Button(self, text="update details", bg="light green", command=self.open_update_details)


    def open_students_list(self):
        window = StudentsList(self)
        window.grab_set()
        self.withdraw()

    def open_lessons_list(self):
        window = LessonsList(self)
        window.grab_set()
        self.withdraw()

    def open_update_details(self):
        window = UpdateDetails(self)
        window.grab_set()
        self.withdraw()