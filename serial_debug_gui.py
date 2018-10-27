#!/usr/bin/python3
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import serial
import datetime
import os

class SerialDebugGui:
    device = None
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("debug_gui.glade")
        self.window = builder.get_object("main_window")
        #self.window.set_default_size(400,400)
        self.device_port = builder.get_object("device_port")
        self.device_baud = builder.get_object("device_baud_rate")
        self.device_txt = builder.get_object("device_setting_text")
        self.device_txt.set_text("Device:")
        self.baud_rate_menu()

    def menu_quite_app(self,winow):
        Gtk.main_quit()

    def baud_rate_menu(self):
        baud_rates = Gtk.ListStore(int,str)
        baud_rates.append([9600,"9600"])
        baud_rates.append([115200,"115200"])
        self.device_baud.new_with_entry()
        

if __name__=="__main__":
    app = SerialDebugGui()
    app.window.connect("delete-event",Gtk.main_quit)
    app.window.show_all()
    Gtk.main()


