import tkinter as tk

class demo1:
    def __init__(self,master):
        self.master=master
        self.frame=tk.Frame(self.master)
        self.button1=tk.Button(self.frame,text="New wind",width=25,command=self.new_wind)
        self.button1.pack()
        self.frame.pack()
    def new_wind(self):
        self.newWind=tk.Toplevel(self.master)
        self.app=demo2(self.newWind)
class demo2:
    def __init__(self,master):
        self.master=master
        self.frame=tk.Frame(self.master)
        self.quitbtn=tk.Button(self.frame,text="Quitme?",width=25,command=self.closewind)
        self.quitbtn.pack()
        self.frame.pack()
    def closewind(self):
        self.master.destroy()

def main():
    root=tk.Tk()
    app=demo1(root)
    root.mainloop()

if __name__ == "__main__":
    main()

