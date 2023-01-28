import tkinter
from tkinter import *
from tkinter import ttk, messagebox


class StudentsList(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('400x400')
        self.title('Students List Screen')
