from tkinter import *
from tkinter import ttk

def button_click():
    pbval.set(pbval.get()+1)
    if pbval.get() > 10:
        pbval.set(0)
if __name__ == '__main__':
    root=Tk()
    #ttk.Style().theme_use('modern')
    root.title('Progress')
    root.columnconfigure(0,weight=1);
    root.rowconfigure(0,weight=1);
    #frame
    frame1=ttk.Frame(root,padding=10)
    frame1.grid(sticky=(N,W,S,E))
    frame1.columnconfigure(0,weight=1);
    frame1.rowconfigure(0,weight=1);
    #progressbar object
    pbval=IntVar(value=3)
    pb=ttk.Progressbar(frame1,orient=HORIZONTAL,variable=pbval,
            maximum=10,length=200,mode='determinate')
    pb.grid(row=0,column=0,sticky=(N,E,S,W))
    # 進捗ボタン
    button1 = ttk.Button(frame1, text='OK', width=5,command=button_click)
    button1.grid(row=0, column=1, padx=5, sticky=(E))
    root.mainloop()


