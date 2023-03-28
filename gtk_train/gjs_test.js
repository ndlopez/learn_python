#!/usr/bin/env gjs;

imports.gi.versions.Gtk = "3.0";
const { Gtk } = imports.gi;

Gtk.init(null);

let dataHome="data/";
let nowTime=new Date();
var currTime=nowTime.getHours().toString()+nowTime.getMinutes().toString();
const button = new Gtk.Button({ label: 'Click Me!' });
button.connect('clicked', () => {
    log('The button was clicked at '+currTime);
});

function readDataFile(fileName){
    try{
        var pathStr=fileName.toString();
        return pathStr;
    }catch(error){
        logError(error,'No such file on storage');
    }
}

const win = new Gtk.Window({ defaultHeight: 600, defaultWidth: 800 });
win.connect('destroy', () => { Gtk.main_quit(); });
win.add(button);
win.show_all();

Gtk.main();