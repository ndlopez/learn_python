import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Hallo work")
        self.box=Gtk.Box(spacing=6)
        self.add(self.box)
        self.btn1=Gtk.Button(label="Hallo")
        self.btn1.connect("clicked",self.on_btn1_clicked)
        self.box.pack_start(self.btn1,True,True,0)
        
        self.btn2=Gtk.Button(label="Goodriddance")
        self.btn2.connect("clicked",self.on_btn2_clicked)
        self.box.pack_start(self.btn2,True,True,0)
    
    def on_btn1_clicked(self,widget):
        print("Hallo workd")
    
    def on_btn2_clicked(self,widget):
        print("goodRiddance")

win=MyWindow()
win.connect("destroy",Gtk.main_quit)
win.show_all()

Gtk.main()
