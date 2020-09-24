from tkinter import *
import tkinter.font as font
import time

class StopWatch(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=5, padx=5)

    def _update(self):
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

    def Start(self):
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1

    def Stop(self):
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

    def Reset(self):
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)


def main():
    root = Tk()
    root.title("Stop Watch")
    root.geometry('400x400')
    sw = StopWatch(root)
    sw.pack()

    Label(root, text=' ').pack()
    Label(root, text=' ').pack()
    Label(root, text=' ').pack()
    Button(root, text='Start', command=sw.Start).pack()
    Label(root, text=' ').pack()
    Button(root, text='Stop', command=sw.Stop).pack()
    Label(root, text=' ').pack()
    Button(root, text='Reset', command=sw.Reset).pack()
    Label(root, text=' ').pack()
    Button(root, text='Quit', command=root.quit).pack()

    root.mainloop()


if __name__ == '__main__':
    main()
