#!/usr/bin/env python3
# create a GUI in Python
from tkinter import *

'''class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_widgets()

        def create_widgets(self):
'''       
#create root window
root =Tk()
#dimensions
root.title("GUI test")
root.geometry('400x300')
#widgets
#menu-bar
myMenu=Menu(root)
root.config(menu=myMenu)
fileMenu=Menu(myMenu)
myMenu.add_cascade(label='File',menu=fileMenu)

fileMenu.add_command(label='New')
fileMenu.add_command(label='Open...')
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=root.quit)
helpMenu=Menu(myMenu)
myMenu.add_cascade(label='Help',menu=helpMenu)
helpMenu.add_command(label='About')
#add a label to root window
Label(root,text='First Name').grid(row=0)
Label(root,text='Last Name').grid(row=1)
entry1=Entry(root)
entry2=Entry(root)
entry1.grid(column=1,row=0)
entry2.grid(column=1,row=1)
lbl=Label(root,text="Are you in?")
lbl.grid(column=0,row=2)
Label(root,text='Languages').grid(row=3)
Label(root,text='OS').grid(row=4)
#list
listBox=Listbox(root)
listBox.grid(column=1,row=3)
myList=["C++","Python","JavaScript","sed/AWK","Ruby"]
for zz in range(len(myList)):
    #print(zz+1,myList[zz])
    listBox.insert(zz+1,myList[zz])

#radiobutton
v=IntVar()
Radiobutton(root, text='Debian 10', variable=v, value=1).grid(column=1,row=4) 
Radiobutton(root, text='Windows 10', variable=v, value=2).grid(column=2,row=4) 

#function to display text when a button is clicked
def click_me():
    res="You wrote: "+txt.get()
    lbl.configure(text = res)

#button widget
btn=Button(root,text="Click me",fg="red",command=click_me)
btn.grid(column=2,row=2) #position on window

#adding entry field
txt=Entry(root,width=10)
txt.grid(column=1,row=2)

root.mainloop()
