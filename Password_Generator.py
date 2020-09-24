from tkinter import *
import random as rd
import pyperclip as pap

root = Tk()
root.title("Password Generator")
root.geometry( '400x400' )

Label(root, text='Enter Number of Characters').pack()

e = Entry(root)
e.pack()

let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['1','2','3','4','5','6','7','8','9']
chars = ['!','@','#','$','%','^','&','8','(',')']

ch = ['let', 'num', 'chars']

def gen():
    password = []
    i = 1
    n = int(e.get())
    while i<=n:
        chs = rd.choice(ch)
        if chs == 'let':
            password.append(rd.choice(let))
        elif chs == 'num':
            password.append(rd.choice(num))
        elif chs == 'chars':
            password.append(rd.choice(chars))
        i+=1

    Label(root, text=' ').pack()
    pase = Entry()
    pase.pack()
    password = ''.join(password)
    pase.insert(0, str(password))
    def copy():
            pap.copy(password)
            Label(root, text="Copied to Clipboard!!!").pack()
    Button(root, text='Copy to Clipboard', command=copy).pack()


sub = Button(root, text='Submit', command=gen)
sub.pack()

root.mainloop()
