#!/usr/bin/env python

import gobject
gobject.threads_init()
import pygtk
pygtk.require('2.0')

from threading import Thread

class GUI(Thread):

    def __init__(self):
        Thread.__init__(self)


    def destroy(self, widget, data=None):
        self.gtk.main_quit()

    def run(self):
        import gtk
        self.gtk = gtk

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.button = gtk.Button("Hello World")
        self.window.add(self.button)
        self.button.show()
        self.window.show()
        
        gtk.main()

gui = GUI()
gui.start()
gui.join()
