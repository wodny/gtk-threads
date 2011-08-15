import multiprocessing

class GUILauncher(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)

    def run(self):
        import gui
        g = gui.GUI()
        g.loop()
