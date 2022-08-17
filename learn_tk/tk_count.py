import time
from tkinter import *
from tkinter import messagebox

#create TK window
root=Tk()
root.geometry("300x250")
root.title("time counter")

hr=StringVar()
mi=StringVar()
sec=StringVar()
hr.set("00")
mi.set("00")
sec.set("00")

hrEntry=Entry(root,width=3,font=("Arial",18,""),textvariable=hr)
hrEntry.place(x=80,y=20)
miEntry=Entry(root,width=3,font=("Arial",18,""),textvariable=mi)
miEntry.place(x=130,y=20)
secEntry=Entry(root,width=3,font=("Arial",18,""),textvariable=sec)
secEntry.place(x=180,y=20)

def submit():
    try:
        temp=int(hr.get())*3600 + int(mi.get())*60+int(sec.get())
    except:
        print("Please input the right value")
    while temp > -1:
        mins,secs=divmod(temp,60)
        hours=0
        if mins > 60:
            hours,mins=divmod(mins,60)
        hr.set("{0:2d}".format(hours))
        mi.set("{0:2d}".format(mins))
        sec.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)

        if (temp==0):
            messagebox.showinfo("Time countdown","Sorry, time's up")
        temp -=1

btn=Button(root,text="set countdown time",bd='5',command=submit)
btn.place(x=70,y=120)
root.mainloop()


