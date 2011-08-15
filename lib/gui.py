import gobject
gobject.threads_init()
# Threads left for future use with a command queue

import pygtk
pygtk.require('2.0')

import gtk

class GUI:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.button = gtk.Button("Hello World")
        self.window.add(self.button)
        self.button.show()
        self.window.show()

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def loop(self):
        gtk.main()
