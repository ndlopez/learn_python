#!/usr/bin/python3.8
import tkinter as tk
from tkinter import ttk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("340x200")
        self.title('Login')
        #self.configure(width=300)
        self.resizable(0,0)
        #config the grid
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)
        self.create_widgets()

    def create_widgets(self):
        #username
        usr_label=ttk.Label(self,text="Username:")
        usr_label.grid(column=0,row=0, sticky=tk.W, padx=5,pady=5)
        usr_entry=ttk.Entry(self)
        usr_entry.grid(column=1,row=0, sticky=tk.E, padx=5,pady=5)
        #password
        pass_label=ttk.Label(self,text="Password:")
        pass_label.grid(column=0,row=1, sticky=tk.W,padx=5, pady=5)
        pass_entry=ttk.Entry(self,show="*")
        pass_entry.grid(column=1,row=1,sticky=tk.E,padx=5,pady=5)
        login_btn=ttk.Button(self,text="Login")
        login_btn.grid(column=1,row=3,sticky=tk.E,padx=5,pady=5)

if __name__ == "__main__":
    app= MyApp()
    app.mainloop()

