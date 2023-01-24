import tkinter

class Login(tkinter.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry('300x100')
        self.title('Toplevel Window 2')
        Button(self, text='Close', command=self.close).pack(expand=True)

    def close(self):
        self.parent.deiconify()
        self.destroy()


