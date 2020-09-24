import names
from tkinter import *

root = Tk()
root.title('Name Generator')
root.geometry('400x400')

Label(root, text='Male Color - ').pack()
Button(root, text='        ', bg='red').pack()
Label(root, text='      ').pack()
Label(root, text='Female Color - ').pack()
Button(root, text='        ', bg='green').pack()
Label(root, text=' ').pack()
Label(root, text=' ').pack()
Label(root, text='Choose Your choice :-').pack()
Label(root, text=' ').pack()

root2 = Tk()
root2.title('Names')
root2.geometry('600x400')

def genm():
    nm = str(names.get_full_name(gender='male'))
    b = Entry(root2, width=30, fg='red')
    b.pack()
    b.insert(0, nm)
    Label(root2, text=' ').pack()

def genf():
    nm = str(names.get_full_name(gender='female'))
    b = Entry(root2, width=30, fg='green')
    b.pack()
    b.insert(0, nm)
    Label(root2, text=' ').pack()

Button(root, text='Male', command=genm, fg='red').pack()
Label(root, text=' ').pack()
Button(root, text='Female', command=genf, fg='green').pack()
Label(root, text=' ').pack()
Label(root, text=' ').pack()
Label(root, text='The Names shall be Displayed on the \n Bigger Window, with the title of Names').pack()

root.mainloop()
