#!/usr/bin/env python

import gobject
gobject.threads_init()

import pygtk
pygtk.require('2.0')

import gtk
gtk.gdk.threads_init()

from threading import Thread

class GUI(Thread):

    def __init__(self):
        Thread.__init__(self)

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.button = gtk.Button("Hello World")
        self.window.add(self.button)
        self.button.show()
        self.window.show()

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def run(self):
        gtk.gdk.threads_enter()
        gtk.main()
        gtk.gdk.threads_leave()

gui = GUI()
gui.start()
gui.join()