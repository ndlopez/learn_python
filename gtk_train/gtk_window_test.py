import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, GLib

import json
#import secrets
#from datetime import date
from ../workers import passphrase, jp2roman

my_words='/home/diego/Templates/pass_adm/static/data/words_list_v2.json'

class MyWindow(Gtk.Window):
    def __init__(self):
        #Gtk.Window.__init__(self,title="Hallo work") <- this works too
        super().__init__(title="My Passphrase Generator")
        self.set_default_size(350,250)
        self.timeoutId=None

        bigBox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        self.add(bigBox)
        #bigBox.set_homogeneous(False)

        topbox=Gtk.Box(spacing=10)
        bigBox.pack_start(topbox,True,True,0)

        myLabel=Gtk.Label(label="Passphrase")
        topbox.pack_start(myLabel,True,True,0)

        self.myEntry=Gtk.Entry()
        self.myEntry.set_text("inolvidable")
        topbox.pack_start(self.myEntry,True,True,10)

        midbox=Gtk.Box(spacing=6)
        bigBox.pack_start(midbox,True,True,0)
        self.check_edit=Gtk.CheckButton(label="Editable")
        self.check_edit.connect("toggled",self.on_editable)
        self.check_edit.set_active(True)
        midbox.pack_start(self.check_edit,True,True,0)
        self.check_visible=Gtk.CheckButton(label="Visible")
        self.check_visible.connect("toggled",self.on_visible)
        self.check_visible.set_active(True)
        midbox.pack_start(self.check_visible,True,True,0)
        self.pulse=Gtk.CheckButton(label="Pulse")
        self.pulse.connect("toggled",self.on_pulse)
        self.pulse.set_active(False)
        midbox.pack_start(self.pulse,True,True,0)
        self.icon=Gtk.CheckButton(label="Icon?")
        self.icon.connect("toggled",self.on_icon)
        self.icon.set_active(False)
        midbox.pack_start(self.icon,True,True,0)

        hbox=Gtk.Box(spacing=10)
        #hbox.set_homogeneous(False)
        bigBox.pack_start(hbox,True,True,10)
        
        self.btn1=Gtk.Button(label="Generate")
        self.btn1.connect("clicked",self.on_btn1_clicked)
        hbox.pack_start(self.btn1,True,True,20)

        self.btn2=Gtk.Button(label="Goodriddance")
        self.btn2.connect("clicked",self.on_btn2_clicked)
        hbox.pack_start(self.btn2,True,False,20)
    
    def on_btn1_clicked(self,widget):
        mypass=passphrase.get_desired_phrase(4,0,20,my_words)

        self.myEntry.set_text(mypass)
        #print("Hallo workd")
    
    def on_btn2_clicked(self,widget):
        print("goodRiddance")
    
    def on_editable(self,button):
        value=button.get_active()
        self.myEntry.set_editable(value)
    
    def on_visible(self,button):
        value=button.get_active()
        self.myEntry.set_visibility(value)
    
    def on_pulse(self,button):
        if button.get_active():
            self.myEntry.set_progress_pulse_step(0.2)
            self.timeoutId=GLib.timeout_add(100,self.do_pulse,None)
        else:
            GLib.source_remove(self.timeoutId)
            self.timeoutId=None
            self.myEntry.set_progress_pulse_step(0)
    
    def do_pulse(self,user_data):
        self.myEntry.progress_pulse()
        return True
    
    def on_icon(self,button):
        if button.get_active():
            icon_name="system-search-symbolic"
        else:
            icon_name=None
        self.myEntry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY,icon_name)

win=MyWindow()
win.connect("destroy",Gtk.main_quit)
win.show_all()

Gtk.main()
