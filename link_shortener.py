import pyshorteners as ps
import pyperclip as pap
from tkinter import *
import webbrowser

""" s = pyshorteners.Shortener()

print(s.tinyurl.short("https://www.google.com")) """

root = Tk()
root.title("Link Shortener")
root.geometry('400x400')

e = Entry(root, width=30)
e.pack()

def shorten():
    try:
        s = ps.Shortener()
        shortened = s.tinyurl.short(str(e.get()))
        b = Entry(root, width=30)
        b.pack()
        b.insert(0, shortened)
        def copy():
            pap.copy(shortened)
            Label(root, text="Copied to Clipboard!!!").pack()
        Button(root, text='Copy to Clipboard', command=copy).pack()
        def open():
            webbrowser.open(shortened)
        Button(root, text='Visit Website', command=open).pack()
    except:
        Label(root, text=' ').pack()
        Label(root, text=' ').pack()
        Label(root, text=' ').pack()
        Label(root, text='Error Occured!!!').pack()

sub = Button(root, text="SHORTEN LINK", command = shorten)
sub.pack()

Label(root, text=' ').pack()

root.mainloop()
