#https://stackoverflow.com/questions/33646605/how-to-access-variables-from-different-classes-in-tkinter

import tkinter as tk
import smtplib

TITLE_FONT = ("Helvetica", 18, "bold")
class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()

    def get_page(self,page_class):#Added 20210310
        return self.frames[page_class]

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PyMail",foreground = "Red", font=("Courier", 30, "bold"))
        label.pack(side="top")
        sublabel = tk.Label(self, text="Bringing you the\n the easiest way of communication",
                            font=("Courier", 15))
        sublabel.pack()

        #wallpaper = tk.PhotoImage(file='Python-logo-notext.gif')
        wallpaper = tk.PhotoImage(file='')
        img = tk.Label(self, image=wallpaper)
        img.image = wallpaper
        img.pack(side="top", expand = True)

        button1 = tk.Button(self, text="Click Here to Login to your account",fg="red",
                            command=lambda: controller.show_frame(PageOne))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack(side="bottom")
        button1.pack(side="bottom")

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        label = tk.Label(self, text="Personal Information", font=TITLE_FONT, foreground="blue")
        label.pack(side="top", fill="x", pady=10)
        global optionv
        self.optionv = tk.StringVar()
        self.optionv.set("---Select One---")
        optionm = tk.OptionMenu(self, self.optionv, "---Select One---", "@gmail.com", "@yahoo.com", "@hotmail.com")

        t1 = tk.Label(self, text="Email Account: ")
        self.v.set("")
        entry1 = tk.Entry(self, textvariable=self.v)
        t2 = tk.Label(self,text="\nPassword: ")
        self.pwd = tk.StringVar()
        self.pwd.set("")
        entry2 = tk.Entry(self, textvariable=self.pwd)
        entry2.config(show="*")
        lgbutton=tk.Button(self, text="Log In", command=self.login) 
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame(StartPage))
        #final = tk.Label(self, textvariable=self.v)
        #finalpwd = tk.Label(self, textvariable=self.pwd)

        t1.pack()
        entry1.pack()
        optionm.pack()
        t2.pack()
        entry2.pack()
        #final.pack()
        #finalpwd.pack()
        lgbutton.pack()
        button.pack(side="bottom")

    def login(self):
        value = tk.Label(self, text="Invalid username / password", font=("Courier", 15, "bold"), foreground="red")
        success = tk.Label(self, text="Login was Successful \n (Click ""Continue"" to compose email)", font=("Courier", 15, "bold"), foreground="blue")
        cbutton = tk.Button(self, text="Continue", command=lambda: self.controller.show_frame(PageTwo))
        status = tk.Label(self, text="Please select your email domain", foreground="red")
        if self.optionv.get() == "@gmail.com":
            try:
                global server
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(self.v.get()+self.optionv.get(), self.pwd.get())
                success.pack()
                cbutton.pack(side="bottom")
            except:
                value.pack() 
        elif self.optionv.get() == "@yahoo.com":
            try:
                server = smtplib.SMTP("smtp.yahoo.com", 587)
                server.ehlo()
                server.starttls()
                server.login(self.v.get()+self.optionv.get(), self.pwd.get())
                success.pack()
                cbutton.pack(side="bottom")
            except:
                value.pack()

        elif self.optionv.get() == "@hotmail.com":
            try:
                server = smtplib.SMTP("smtp.live.com", 587)
                server.ehlo()
                server.starttls()
                server.login(self.v.get()+self.optionv.get(), self.pwd.get())
                success.pack()
                cbutton.pack(side="bottom")
            except:
                value.pack()
        else:
            status.pack()

class PageTwo(tk.Frame): 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller#added 20210310
        label = tk.Label(self, text="Compose Mail", font=TITLE_FONT, foreground="green") 
        label.pack(side="top", fill="x", pady=10)

        self.reciever = tk.StringVar()
        self.reciever.set("")
        senderl = tk.Label(self, text="Send to: ")
        rmail = tk.Entry(self, textvariable=self.reciever)

        self.senderoption = tk.StringVar()
        self.senderoption.set("---Select One---")
        senderdomain = tk.OptionMenu(self, self.senderoption, "---Select One---", "@gmail.com", "@hotmail.com", "@yahoo.com")

        self.mail = tk.StringVar()
        self.mail.set("")
        self.textw = tk.Entry(self, textvariable=self.mail)

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame(StartPage))

        sendbutton = tk.Button(self, text = "Send Mail", command=self.sendmail)

        senderl.pack(side="top", anchor="w")
        rmail.pack(side="top", anchor="nw")
        senderdomain.pack(side="top", anchor="nw")
        self.textw.pack(fill="both")
        button.pack(side="bottom")
        sendbutton.pack(side="bottom")
        #Added 20210310
        page1=self.controller.get_page(PageOne)
        page1.v.set("Helloworld?")
        
    def sendmail(self):
        sent = tk.Label(self, text="Email has been sent")
        if self.senderoption.get() == "@gmail.com":
            try: 
                server.sendmail(self.v.get()+self.optionv.get(), self.reciever.get()+self.senderoption.get(), "YES")
                print("Success")
                sent.pack()
            except:
                print("Unsuccesful")
                print(PageOne.self.v.get())

if __name__ == "__main__":
    app = SampleApp()
    app.title("PyMail")
    app.geometry("400x400")
    app.mainloop()
