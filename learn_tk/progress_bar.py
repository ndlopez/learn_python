import tkinter
from tkinter import ttk
import time

class testProgress(ttk.LabelFrame):
    def __init__(self,master=None):
        super().__init__(master,text="Progressbar")
        #progressbar object
        self.progress= ttk.Progressbar(self)
        self.progress.configure(value=0,mode='determinate',maximum=100)
        self.progress.pack()
        #start button
        self.start_button=ttk.Button(self,command=self.startbart,text='Load')
        self.start_button.pack()
        #stop button
        self.stop_button=ttk.Button(self,command=self.stopbart,text='Stop')
        self.stop_button.pack()
    def startbart(self):
        i=1
        while i<=100:
            self.progress.configure(value=i)
            self.progress.update()
            i +=1
            time.sleep(0.02)
        print("Coundown is over",i)
    def stopbart(self):
        print("Instant stop")
        self.progress.stop()
if __name__ == "__main__":
    root =tkinter.Tk()
    f=testProgress(master=root)
    f.pack()
    root.mainloop()

