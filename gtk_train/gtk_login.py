import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class LoginWindow(Gtk.Window):
    def __init__(self,parent):
        super().__init__(title="Login")
        #self.set_default_size(200,200)
        
        ingrid=Gtk.Grid()
        self.add(ingrid)

        usrLbl=Gtk.Label(label="Username")
        passLbl=Gtk.Label(label="Passphrase")
        usrEntry=Gtk.Entry()
        passEntry=Gtk.Entry()
        loginBtn=Gtk.Button(label="Login")
        cancelBtn=Gtk.Button(label="Cancel")
        #cancelBtn.connect("clicked",)

        ingrid.add(usrLbl)
        #within: child, left, top, width, height 
        #ingrid.attach(usrEntry,1,0,2,1)
        ingrid.attach_next_to(usrEntry,usrLbl,Gtk.PositionType.RIGHT,1,1)
        #within: child, sibling, left, top, width, height
        ingrid.add(passLbl)
        #ingrid.attach_next_to(passLbl,usrLbl,Gtk.PositionType.BOTTOM,1,2)
        ingrid.attach_next_to(passEntry,passLbl,Gtk.PositionType.RIGHT,1,1)

        ingrid.attach(loginBtn,0,2,1,1)
        ingrid.attach_next_to(cancelBtn,loginBtn,Gtk.PositionType.RIGHT,1,1)

        self.show_all()

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Main Program")
        self.set_border_width(6)
        self.set_default_size(300,250)
        myBtn=Gtk.Button(label="Hello & Goodbye")
        myBtn.connect("clicked",self.on_btn_clicked)
        self.add(myBtn)
    
    def on_btn_clicked(self,widget):
        logMe=LoginWindow(self)
        #logMe.destroy()

win=MainWindow()
win.connect("destroy",Gtk.main_quit)
win.show_all()

Gtk.main()


