import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from DriveProject.server_d.teacherdb import TeacherDb
from DriveProject.server_d.studentdb import StudentDb
import threading

class MenuTeacher(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('500x500')
        self.title('Menu Teacher Screen')

