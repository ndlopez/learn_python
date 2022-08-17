# create a GUI in Python
from tkinter import *
import tkinter as tk
import re

#create root window
root =Tk()
#dimensions
root.title("GUI test")
root.geometry('400x300')

errmsg = StringVar()
formatmsg = "Zip should be ##### or \n#####-####"

def check_zip(newval, op):
    errmsg.set('')
    valid = re.match('^[0-9]{5}(\-[0-9]{4})?$', newval) is not None
    #valid = re.match('^[0-9]{2}?$', newval) is not None
    btn['state']=tk.NORMAL if valid else tk.DISABLED
    if op=='key':
        ok_so_far = re.match('^[0-9\-]*$', newval) is not None and len(newval) <= 10
        if not ok_so_far:
            msg.configure(foreground="red")
            errmsg.set(formatmsg)
        return ok_so_far
    elif op=='focusout':
        if not valid:
            errmsg.set(formatmsg)
    return valid

def success_func():
    msg.configure(foreground="black")
    return errmsg.set("Postal address OK")

check_zip_wrapper = (root.register(check_zip), '%P', '%V')

zip = StringVar()
#f = ttk.Frame(root)
#f.grid(column=0, row=0)
tk.Label(root, text='Name:').grid(column=0, row=0, padx=5, pady=5)
tk.Entry(root).grid(column=1, row=0, padx=5, pady=5)
tk.Label(root, text='Zip:').grid(column=0, row=1, padx=5, pady=5)

e =tk.Entry(root, textvariable=zip, validate='all', validatecommand=check_zip_wrapper)
e.grid(column=1, row=1, padx=5, pady=5)

btn = tk.Button(root, text="Process",command=success_func)
btn.grid(column=1, row=2, padx=5, pady=5)
btn['state']=tk.DISABLED
msg = tk.Label(root, font='TkLargeCaptionFont', textvariable=errmsg)
msg.grid(column=1, row=3, padx=5, pady=5, sticky='w')

tk.Button(root,text="Exit",command=root.destroy).grid(column=2,row=2)

root.mainloop()
