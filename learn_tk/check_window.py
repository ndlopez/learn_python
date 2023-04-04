from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Check ur result")

data=[("Candice","passed"),("Brooke","failed")]

def check_result():
    myMsg=["Congratulations ","Sorry "]
    for i in data:
        if i[0]==entry.get():
            #if entry test matches
            if i[1]=="passed":
                var=myMsg[0]+i[0]
                messagebox.showinfo("Info",var+",  You have passed")
            else:
                var=myMsg[1]+i[0]
                messagebox.showwarning("Info",var+", You have failed")
            return

    #this will run if an error occurred
    messagebox.showerror("Error","Invalid name or not in the database.")
    entry.delete(0,END)

def clear_entry():
    entry.delete(0,END)

def exit_prog():
    confirm=messagebox.askquestion("Confirm","Are you sure you want to exit?")
    if confirm=='Yes':
        #window.destroy()
        quit()
    else:
        print("return to window")
        return

entry=Entry(window)
entry.pack()

Button(window,text="Check result",command=check_result).pack()
Button(window,text="Clear",command=clear_entry).pack(side=LEFT)
Button(window,text="Exit",command=exit_prog).pack(side=LEFT)

window.mainloop()
