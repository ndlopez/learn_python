''' 
A simple Tkinter program
test if tkinter is properly installed:
$ python3.8 -m tkinter
if a simple Tcl/Tk GUI interface is shown then ok
'''
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello world\n (click me)"
        self.hi_there["command"]=self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self,text="Quit",fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    #Display a msg on terminal, not GUI
    def say_hi(self):
        print("hello there, everyoen")

root=tk.Tk()
app=App(master=root)
app.mainloop()
