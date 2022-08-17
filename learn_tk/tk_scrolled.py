#!/usr/bin/python3.7
from tkinter import *
from tkscrolledframe import ScrolledFrame

root=Tk()
mySF=ScrolledFrame(root,width=640,height=480)
mySF.pack(side="top",expand=1,fill="both")
#bind arrow keys and scroll whell
mySF.bind_arrow_keys(root)
mySF.bind_scroll_wheel(root)
#create a frame within the scrolledframe
inner_frame=mySF.display_widget(Frame)
#add widgets
nrows=16
ncols=10
for row in range(nrows):
    for col in range(ncols):
        wg = Label(inner_frame,width=15,height=5,borderwidth=2,relief="groove",anchor="center",justify="left",text=str(row*nrows+col))
        wg.grid(row=row,column=col,padx=4,pady=4)

#start tk event loop

root.mainloop()
