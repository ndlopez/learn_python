from tkinter import *

from login import Login, Register

class MainWindow:
    def __init__(self):
        self.app=Tk()
        self.app.title("Login windoq")
        self.app.geometry("300x300")
        self.create_widgets()

    def create_widgets(self):
        self.label=Label(self.app,text='Welcome to app')
        self.label.place(x=95,y=40)
        self.login=Button(self.app,text="Login",command=login)
        self.login.place(x=100,y=100)
        self.register=Button(self.app,text="Regisyer",command=register)
        self.register.place(x=100,y=150)
        Button(self.app,text="Close",command=self.app.destroy).place(x=100,y=200)
    def run(self):
        self.app.mainloop()

def login():
    loginTk=Login()
    loginTk.run()

def register():
    registerTk=Register()
    registerTk.run()

app = MainWindow()
app.run()
