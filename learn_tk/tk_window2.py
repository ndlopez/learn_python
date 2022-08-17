#!/usr/bin/python3.8
import tkinter as tk
from tkinter import *
root = Tk()

root.configure(background='yellow')
root.geometry('600x450')

label=Label(root,text="Welcome to tkinter")
label.pack(pady=10)

def btn_trigger():
	print("Button pressed")
btn=Button(root,text="press button",foreground="green",command=btn_trigger)
btn.pack(pady=10)

def chk_btn_action():
	print(chk_btn_var.get())
	if chk_btn_var.get()==1:
		root.configure(background='white')
	else:
		root.configure(background='black')

chk_btn_var=IntVar()
chk_btn=tk.Checkbutton(root,text="on/off",variable=chk_btn_var,command=chk_btn_action)
chk_btn.pack(pady=5)

entry_frame=Frame(root,borderwidth=3,relief=SUNKEN)
entry_frame.pack()

txt_box=Entry(entry_frame)
txt_box.pack()

def get_entry_txt():
	print(txt_box.get())
	root.geometry('600x600')
	label.configure(text=txt_box.get())
	slide_frame.pack(pady=10)

btn2=Button(entry_frame,text="get entry",command=get_entry_txt)
btn2.pack(pady=5)

bill_amount_entry=txt_box
#bill_amount_entry.append(txt_box)
slide_frame=Frame(root,borderwidth=5,relief=SUNKEN)
slide_frame.pack_forget()
Label(slide_frame,text="Total bill").pack() #grid(row=6,column=1)
bill_wtip=Label(slide_frame)
bill_wtip.pack() #grid(row=6,column=2)
def calc_total_bill(value):
	print(value,bill_amount_entry.get())
	if bill_amount_entry.get() != ' ':
		tip_perc=float(value)
		bill=float(bill_amount_entry.get())
		tip_amount=tip_perc*bill
		#text=f'(bill+tip_amount)'
		print("total bill",tip_amount+bill)
		bill_wtip.configure(text=str(bill+tip_amount))

slider=Scale(slide_frame,from_=0.00,to=1.0,orient=HORIZONTAL,length=400,tickinterval=0.1,resolution=0.01, command=calc_total_bill)
slider.pack()
lstbox_frame=Frame(root,borderwidth=5,relief=SUNKEN)
lstbox_frame.pack(pady=5)
lstbox=Listbox(lstbox_frame)
lstbox.pack()
lstbox.insert(END,"eins")
for item in ["zwei","drei","vier","funf"]:
	lstbox.insert(END,item)
lst_box_lbl=Label(root,text="")
lst_box_lbl.pack()

def lst_item_sel():
	root.geometry('600x800')
	selection=lstbox.curselection()
	if selection:
		print(lstbox.get(selection[0]))
		lst_box_lbl.configure(text=lstbox.get(selection[0]))
	radio_buttons.pack()
lst_box_btn=Button(lstbox_frame,text='list item button',command=lst_item_sel)
lst_box_btn.pack()

Label(root,text="choose icon")
def radio_btn_func():
	print(rb_icon_var.get())
	if rb_icon_var.get() ==1:
		radio_btn_icon.configure(text='\u26F0')
	elif rb_icon_var.get() ==2:
		radio_btn_icon.configure(text='\u26F5')
	elif rb_icon_var.get()==3:
		radio_btn_icon.configure(text='\u26FA')

rb_icon_var=IntVar()
radio_buttons=Frame(root)
radio_buttons.pack_forget()
Radiobutton(radio_buttons,text="mountains",variable=rb_icon_var,value=1,command=radio_btn_func).pack()
Radiobutton(radio_buttons,text="boating",variable=rb_icon_var,value=2,command=radio_btn_func).pack()
Radiobutton(radio_buttons,text="camping",variable=rb_icon_var,value=3,command=radio_btn_func).pack()
radio_btn_icon=Label(radio_buttons,text=' ',font=("Helvetica",150))
radio_btn_icon.pack()

root.mainloop()
