import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,GLib

class progressBarWind(Gtk.Window):
    def __init__(self):
        super().__init__(title="ProgressBar demo")
        self.set_border_width(10)

        vbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
        self.add(vbox)

        self.myProgBar=Gtk.ProgressBar()
        vbox.pack_start(self.myProgBar,True,True,0)

        mychktxt=Gtk.CheckButton(label="Show text")
        mychktxt.connect("toggled",self.on_show_text)
        vbox.pack_start(mychktxt,True,True,0)

        mychkact=Gtk.CheckButton(label="Activity mode")
        mychkact.connect("toggled",self.on_activ_mode)
        vbox.pack_start(mychkact,True,True,0)

        mychkRL=Gtk.CheckButton(label="R -> L")
        mychkRL.connect("toggled",self.on_right2left)
        vbox.pack_start(mychkRL,True,True,0)

        self.timeoutID=GLib.timeout_add(50,self.on_timeout,None)
        self.activ_mode=False

    def on_show_text(self,button):
        show_text=button.get_active()
        if show_text:
            text="any text"
        else:
            text=None
        self.myProgBar.set_text(text)
        self.myProgBar.set_show_text(show_text)
    
    def on_activ_mode(self,button):
        self.activ_mode=button.get_active()
        if self.activ_mode:
            self.myProgBar.pulse()
        else:
            self.myProgBar.set_fraction(0.0)
    
    def on_right2left(self,button):
        value=button.get_active()
        self.myProgBar.set_inverted(value)

    def on_timeout(self,user_data):
        #update value on the progress bar
        if self.activ_mode:
            self.myProgBar.pulse()
        else:
            new_value=self.myProgBar.get_fraction()+0.01
            if new_value > 1:
                new_value=0
            self.myProgBar.set_fraction(new_value)
        #as this is a timeout fraction, return True 
        #so it continues to get called
        return True

win=progressBarWind()
win.connect("destroy",Gtk.main_quit)
win.show_all()
Gtk.main()
