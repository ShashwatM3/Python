from tkinter import *
import random as rd
import tkinter as tk
import tkinter.font as font

root = Tk()
root.title("Math Games")
root.geometry('400x500')
root.background='black'
Label(root, text=' ').pack()

noe = [*range(101, 201)]
nom = [*range(301,401)]
noh = [*range(701, 1001)]

yes = ['Congrats!!! Very well Done!', 'Wooohoooo, THAT IS CORRECT!', 'Well Chosen, YOU ARE CORRECT']
nono = ['Oh no! Looks like you got it wrong!', 'Are you sure about tht? Try doing it again.', 'Incorrect. Better Luck next time']

re = [*range(1,5)] 

fontt2 = font.Font(family='fixedsys', size=30, weight='bold')
fontm = font.Font(family='fixedsys', size=25, overstrike=40)

font_normal = font.Font(family='Helvetica', size=25, overstrike=40)

Label(root, text='+ -\n % *', font=fontt2).pack()
Label(root, text='_________________________________________________________').pack()
Label(root, text='Math It Up', font=fontm).pack()

def start():
    rootm=Tk()
    rootm.geometry('400x400')
    rootm.title('Math It Up')
    Label(rootm, text=' ').pack()
    Label(rootm, text=' ').pack()
    Label(rootm, text=' ').pack()
    Label(rootm, text=' ').pack()
    fontt2 = font.Font(family='opensans', size=25)
    fontm = font.Font(family='fixedsys', size=25, overstrike=40)
    Label(rootm, text='Choose level :- ', font=fontt2).pack()
    Label(rootm, text='_________________________________________________________').pack()

    def easy():
        roote = Tk()
        roote.title("Math It Up! - Easy")
        roote.geometry('400x400')

        Label(roote, text='+ -\n* %').pack()
        Label(roote, text='_________________________________________________________').pack()
        Label(roote, text=' ').pack()
        number = rd.choice(noe)
        Label(roote, text='Number Generated - '+str(number)).pack()
        Label(roote, text=' ').pack()

        ne1 = Entry(roote)
        ne1.pack()

        Label(roote, text=' ').pack()

        ne2 = Entry(roote)
        ne2.pack()

        Label(roote, text=' ').pack()

        ne3 = Entry(roote)
        ne3.pack()

        Label(roote, text=' ').pack()

        def calceas():
            no1e = float(ne1.get())
            no2e = float(ne2.get())
            no3e = float(ne3.get())

            if (no1e not in re and no1e % 10 != 0) and (no2e not in re and no2e % 10 != 0) and (no3e not in re and no3e % 10 != 0):
                if float(no1e*no2e*no3e) == float(number):
                    Label(roote, text=rd.choice(yes)).pack()
                else:
                    Label(roote, text=rd.choice(nono)).pack()
            else:
                Label(roote, text='Remember that the number should not be in range from 1 to 4 \n and cannot be a multiple of 10').pack()

        Button(roote, text='Submit', command=calceas).pack()

        roote.mainloop()

    def med():
        rootmed = Tk()
        rootmed.title("Math It Up! - Easy")
        rootmed.geometry('400x400')

        try:
            rootmed.after(10000, lambda: rootmed.destroy())
        except:
            pass

        Label(rootmed, text='+ -\n* %').pack()
        Label(
            rootmed, text='_________________________________________________________').pack()
        Label(rootmed, text=' ').pack()
        number = rd.choice(nom)
        Label(rootmed, text='Number Generated - '+str(float(number))).pack()
        Label(rootmed, text=' ').pack()

        n1 = Entry(rootmed)
        n1.pack()

        Label(rootmed, text=' ').pack()

        n2 = Entry(rootmed)
        n2.pack()

        Label(rootmed, text=' ').pack()

        n3 = Entry(rootmed)
        n3.pack()

        Label(rootmed, text=' ').pack()

        n4 = Entry(rootmed)
        n4.pack()

        Label(rootmed, text=' ').pack()

        def calcmed():
            no1 = float(n1.get())
            no2 = float(n2.get())
            no3 = float(n3.get())
            no4 = float(n4.get())

            if (no1 not in re and no1 % 10 != 0) and (no2 not in re and no2 % 10 != 0) and (no3 not in re and no3 % 10 != 0) and (no4 not in re and no4 % 10 != 0):
                if float(no1*no2*no3*no4) == float(number):
                    Label(rootmed, text=rd.choice(yes)).pack()
                else:
                    Label(rootmed, text=rd.choice(nono)).pack()
            else:
                Label(rootmed, text='Remember that the number should not be in range from 1 to 4 \n and cannot be a multiple of 10').pack()

        Button(rootmed, text='Submit', command=calcmed).pack()

        rootmed.mainloop()

    def hard():
        rooth = Tk()
        rooth.title("Math It Up! - Easy")
        rooth.geometry('400x400')

        Label(rooth, text='+ -\n* %').pack()
        Label(
            rooth, text='_________________________________________________________').pack()
        Label(rooth, text=' ').pack()
        number = rd.choice(noh)
        Label(rooth, text='Number Generated - '+str(number)).pack()
        Label(rooth, text=' ').pack()

        nh1 = Entry(rooth)
        nh1.pack()

        Label(rooth, text=' ').pack()

        nh2 = Entry(rooth)
        nh2.pack()

        Label(rooth, text=' ').pack()

        nh3 = Entry(rooth)
        nh3.pack()

        Label(rooth, text=' ').pack()

        nh4 = Entry(rooth)
        nh4.pack()

        Label(rooth, text=' ').pack()

        nh5 = Entry(rooth)
        nh5.pack()

        Label(rooth, text=' ').pack()

        def calceas():
            no1 = float(nh1.get())
            no2 = float(nh2.get())
            no3 = float(nh3.get())
            no4 = float(nh4.get())
            no5 = float(nh5.get())

            if (no1 not in re and no1 % 10 != 0) and (no2 not in re and no2 % 10 != 0) and (no3 not in re and no3 % 10 != 0):
                if float(no1*no2*no3) == float(number):
                    Label(rooth, text=rd.choice(yes)).pack()
                else:
                    Label(rooth, text=rd.choice(nono)).pack()
            else:
                Label(rooth, text='Remember that the number should not be in range from 1 to 4 \n and cannot be a multiple of 10').pack()

        Button(rooth, text='Submit', command=calceas).pack()

        rooth.mainloop()

    Label(rootm, text=' ').pack()
    Button(rootm, text='Easy', command=easy, font=fontm, bg='yellow').pack()
    Label(rootm, text=' ').pack()
    Button(rootm, text='Medium', command=med, font=fontm, bg='orange').pack()
    Label(rootm, text=' ').pack()
    Button(rootm, text='Hard', command=hard, font=fontm, bg='red').pack()


    """
    try:
        rootm.after(10000, lambda: rootm.destroy())
    except:
        pass

    """

    Label(rootm, text=' ').pack()
    Label(rootm, text='_________________________________________________________').pack()
    rootm.mainloop()

def about():
    rootab = Tk()
    rootab.geometry('400x400')
    rootab.title('About - Math It Up')
    Label(rootab, text=' ').pack()
    Label(rootab, text=' ').pack()
    Label(rootab, text=' ').pack()
    Label(rootab, text=' ').pack()
    Label(rootab, text='---------------------------------------------------------').pack()
    Label(rootab, text='____About____').pack()
    Label(rootab, text=' ').pack()
    Label(rootab, text='This Application has been coded and built by Shashwat Mahalanobis. \n This application contains mathematical games \n that improves your brain\'s functionalality in mathematical activities.').pack()
    Label(root, text=' ').pack()
    Label(rootab, text='---------------------------------------------------------').pack()
    rootab.mainloop()


def docs():
    rootd = Tk()
    rootd.geometry('400x500')
    rootd.title('How to play - Math It Up')
    Label(rootd, text='---------------------------------------------------------').pack()
    Label(rootd, text='____How to Play____').pack()
    Label(rootd, text=' ').pack()
    Label(rootd, text='In this game, there are 3 levels in Math It Up :- \n\nEasy \n Medium \n Hard \n\n In this game, the application will generate a random number \n depending on the level. \n\n So for EASY, the random number shall be generated from 1 to 50 \n For MEDIUM, the random number shall be generated from 51 to 100 \n For HARD, the random number shall be generated from 101 to 200. \n\n Then the text boxes will be generated based upon the level, So :- \n\n Easy - 3 text boxes \n Medium - 4 text boxes \n Hard - 5 text boxes\n\n in which you will have to \n type numbers (the numbers can also be decimals) \n whose product will be the random number generated, \n within the time limit (will be decided upon the level)  \n otherwise the window shall  \n exit on it\'s own. \n However, the number the user types cannot \n be from 0 to 4 and cannot be a multiple of 10 \n\n GOOD LUCK!!!').pack()
    Label(rootd, text='---------------------------------------------------------').pack()
    rootd.mainloop()

Label(root, text='_________________________________________________________').pack()
Label(root, text=' ').pack()

fontt = font.Font(family='opensans', size=12, weight='bold')
Button(root, text='Play', command=start, bg='blue', fg='white', font=fontt).pack()
Label(root, text=' ').pack()
Button(root, text='How to Play', command=docs,
       bg='blue', fg='white', font=fontt).pack()
Label(root, text=' ').pack()
Button(root, text='About', command=about,
       bg='blue', fg='white', font=fontt).pack()
Label(root, text=' ').pack()
Label(root, text='_________________________________________________________').pack()
Label(root, text='+ -\n % *', font=fontt2).pack()
root.mainloop()
