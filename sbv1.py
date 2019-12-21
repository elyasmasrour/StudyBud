#IMPORTS
import time
import tkinter as tk
import random
import os

def initialize():
    button.pack_forget()
    studytimer(10)


def studytimer(timer):
    global block
    block=0
    pauseplay.configure(image=pause2)
    count_down(timer,1 )

def sleep():
    global block
    block=1
    pauseplay.configure(image='')
    quote.configure(text='')
    countdowntimer.configure(text = '')


def breaktime():
    pauseplay.configure(image='')
    quote.configure(text='Great job! Take a quick break. ')
    count_down(10, 2)


def count_down(timer, type):
    global block
    global temptimer
    countdowntimer.configure(font=('arial',40, 'bold'))
    if (type==1):
        color(2)
        quote.configure(text=motivation[random.randint(0,2)])
        for t in range(timer, -1, -1):
            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
            countdowntimer.configure(text = sf)
            time_str.set(sf)
            root.update()
            timer = timer-1
            st=str(sf)
            if (st=="00:00"):
                break
            if (st[3:5]=="31"):
                quote.configure(text=motivation[random.randint(0,2)])
            if (st[3:5]=="01"):
                quote.configure(text=motivation[random.randint(0,2)])
            if (block==1):
                temptimer=timer
                break
            time.sleep(1)
        if (block==0):
            breaktime()

    else:
        color(1)
        for t in range(timer, -1, -1):
            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
            countdowntimer.configure(text = sf)
            time_str.set(sf)
            root.update()
            timer = timer-1
            st=str(sf)
            if (st=="00:00"):
                break
            time.sleep(1)
        studytimer(100)

def pause():
    global block
    global temptimer
    if(block==0):
        block=1
        pauseplay.config(image = play)

    else:
        block=0
        pauseplay.config(image = pause2)
        count_down(temptimer,1)

def color(c):
    if(c==1):
        screen.config(background="#4A7856")
        quote.config(bg="#4A7856")
        countdowntimer.configure(bg="#4A7856")
        pauseplay.config(bg="#4A7856")

    if(c==2):
        screen.config(background="#2C666E")
        quote.config(bg="#2C666E")
        countdowntimer.configure(bg="#2C666E")
        pauseplay.config(bg="#2C666E")

#NECESSARY
root = tk.Tk()
root.title("StudyBuddy")
root.geometry('320x480')
root.configure(background='gray')
time_str = tk.StringVar()

#VARIABLE PRESETS

f = open(os.path.join(os.getcwd(), "assets", "motivational_quotes.txt"))
block=0
motivation = [line for line in f.readlines()]

#WIDGETS

screen = tk.Frame(root, width = 320, height = 450)
screen.grid(row=0, column = 0)
screen.config(background="#2C666E")
screen.pack_propagate(0)


console = tk.Frame(root, width = 320, height = 450)
console.grid(row=1, column = 0)
console.config(background="#FFFFFF")
button = tk.Button(console, text='Program Begin', command=lambda: initialize())
button.pack(side = 'left')
button2 = tk.Button(console, text='Sleep', command=sleep).pack(side = 'right')

countdowntimer = tk.Label(screen, text = "", font=('arial', 100, 'bold'), bg = "#2C666E")
countdowntimer.place(x=85,y=150, width=150)

quote = tk.Label(screen, text = "",font=('trade gothic',10, 'bold'), bg = "#2C666E")
quote.place(x=10, y=210, width =300)


play = tk.PhotoImage(file= os.path.join(os.getcwd(), "assets", "play.png"))
pause2 = tk.PhotoImage(file=os.path.join(os.getcwd(), "assets", "pause.png"))


pauseplay = tk.Button(screen, command=pause, borderwidth = 0, highlightthickness = 0, bg = "#2C666E")
pauseplay.place(x=130, y=250)

#EXPERIMENTAL


#REQUIRED
root.wm_attributes('-fullscreen','true')
root.mainloop()
