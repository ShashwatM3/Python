import qrcode
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title('QR Code Generator')
root.geometry('700x500')


Label(root, text=' ').pack()
Label(root, text=' ').pack()
Label(root, text=' ').pack()
Label(root, text=' ').pack()
Label(root, text=' ').pack()
Label(root, text=' ').pack()
Label(root, text=' ').pack()
Label(root, text=' ').pack()

Label(root, text="Copy the link from the browser and paste it here - ").pack()

inpu = Entry(root, width='100')
inpu.pack()

def generate():
    inp = str(inpu.get())
    im = qrcode.make(inp)
    im.save('te')
    im.show()
    
sub = Button(root, text='submit', command=generate)
sub.pack()

root.mainloop()
