import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class DialogExample(Gtk.Dialog):
    def __init__(self,parent):
        super().__init__(title="Information dialog",transient_for=parent,flags=0)
        self.add_buttons(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_OK,Gtk.ResponseType.OK)
        self.set_default_size(150,100)
        thisLabel=Gtk.Label(label="This is a dialog to display additional info")
        thisBox=self.get_content_area()
        thisBox.add(thisLabel)
        self.show_all()

class DialogWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="A diaglof example")
        self.set_border_width(6)
        self.set_default_size(250,200)
        myBtn=Gtk.Button(label="Open dialog")
        myBtn.connect("clicked",self.on_button_clicked)
        self.add(myBtn)
    
    def on_button_clicked(self,widget):
        dialog=DialogExample(self)
        response=dialog.run()
        if response == Gtk.ResponseType.OK:
            print("the ok button was clicked")
        elif response == Gtk.ResponseType.CANCEL:
            print("the cancel button was clicked")
        
        dialog.destroy()

win=DialogWindow()
win.connect("destroy",Gtk.main_quit)
win.show_all()
Gtk.main()

