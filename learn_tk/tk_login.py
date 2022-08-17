#login.py
from tkinter import *
from tkinter import messagebox
#import bcrypt
#from database import Database

#db=Database()
#db.createTable()

class Login:
    def __init__(self):
        self.loginWindow=Tk()
        self.loginWindow.title("Login with ")
        self.loginWindow.geometry("300x250")
        self.create_widgets()

    def create_widgets(self):
        self.label=Label(self.loginWindow,text="Logme in")
        self.label.place(x=95,y=40)
        self.user=StringVar()
        self.pasw=StringVar()
        self.usernameE=Entry(self.loginWindow,textvariable=self.user)
        self.usernameE.place(x=70,y=80)
        self.passwordE=Entry(self.loginWindow,textvariable=self.pasw,show='*')
        self.passwordE.place(x=70,y=120)

        self.username=self.user.get()
        self.paswd=self.pasw.get()
        
        self.submit=Button(self.loginWindow,text="Submit",command=self.validate)
        self.submit.place(x=100,y=150)
        Button(self.loginWindow,text="Close",command=self.loginWindow.destroy).place(x=150,y=150)
    
    def validate(self):
        pass
        '''data=(self.username,)
        inputData=(self.username,self.paswd)
        try:
            if (db.validateData(data,inputData)):
                tk.messagebox.showinfo("Successfull","Login was successfull")
            else:
                tk.messagebox.showerror("Error","Wrong credentials")
        '''
    def run(self):
        self.loginWindow.mainloop()

class Register:
    def __init__(self):
        self.registerWindow=Tk()
        self.registerWindow.title("Register to pas")
        self.registerWindow.geometry("300x400")
        self.label=Label(self.registerWindow,text="REgister")
        self.label.place(x=95,y=40)
        self.user=StringVar()
        self.pasw=StringVar()
        self.usernameE=Entry(self.registerWindow,textvariable=self.user)
        self.usernameE.place(x=70,y=80)
        self.passwordE=Entry(self.registerWindow,textvariable=self.pasw,show='*')
        self.passwordE.place(x=70,y=120)
    def run(self):
        self.registerWindow.mainloop()
