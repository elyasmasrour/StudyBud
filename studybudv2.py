#IMPORTS
import time
import tkinter as tk
import random
import simpleaudio as sa
import os

def initialize():
    notif.config(text = "Would you like music?")
    countdowntimer.place_forget()
    no.place(x=95,y=150)
    yes.place(x=160, y=150)

def nomusic():
    no.place_forget()
    yes.place_forget()
    notif.place_forget()
    countdowntimer.place(x=ctdpx,y=ctdpy, width=320)
    studytimer(10)

def yesmusic():
    fastforward.place(x=ffpx, y=ffpy)
    rewindbutton.place(x=rwx, y=rwy)
    currentmusic.place(x=cmx, y=cmy)
    musiccontrol.place(x=0, y=330)
    no.place_forget()
    yes.place_forget()
    notif.place_forget()
    countdowntimer.place(x=ctdpx,y=ctdpy, width=320)
    music.play()
    studytimer(10)

def studytimer(timer):
    sound2.play()
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
    fastforward.place_forget()
    musiccontrol.place_forget()

def breaktime():
    sound3.play()
    pauseplay.configure(image='')
    quote.configure(text='Great job! Take a quick break. ')
    count_down(10, 2)

def count_down(timer, type):
    global block
    global temptimer
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
    sound1.play()
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
        screen.config(background="#5271ff")
        quote.config(bg="#5271ff")
        countdowntimer.configure(bg="#5271ff")
        pauseplay.config(bg="#5271ff")
        fastforward.configure(image=forward2)
        rewindbutton.configure(image=rewind2)
        currentmusic.configure(image=violin2)

    if(c==2):
        screen.config(background="#FFFFFF")
        quote.config(bg="#FFFFFF")
        countdowntimer.configure(bg="#FFFFFF")
        pauseplay.config(bg="#FFFFFF")
        fastforward.configure(image=forward)

#NECESSARY
root = tk.Tk()
root.title("StudyBuddy")
root.geometry('320x480')
root.configure(background='gray')
time_str = tk.StringVar()

#VARIABLE PRESETS
qpx, qpy= 0, 165
ctdpx, ctdpy= 0, 50
block=0
ppx, ppy= 124, 200
ffpx, ffpy= 224, 340
rwx, rwy= 0, 340
cmx, cmy= 112, 340
motivation= ["Keep working! It's worth it.", "Hard work is the key to success.", "Do or do not. There is no try"]

#WIDGETS

screen = tk.Frame(root, width = 320, height = 450)
screen.grid(row=0, column = 0)
screen.config(background="#FFFFFF")
screen.pack_propagate(0)


console = tk.Frame(root, width = 320, height = 450)
console.grid(row=1, column = 0)
console.config(background="#FFFFFF")
button = tk.Button(console, text='Program Begin', command=lambda: initialize()).pack(side = 'left')
sleepbutton = tk.Button(console, text='Sleep', command=sleep).pack(side = 'right')

countdowntimer = tk.Label(screen, text = "",font=('trade gothic',80, 'bold'), bg = "#FFFFFF")
countdowntimer.place(x=ctdpx,y=ctdpy, width=320)

quote = tk.Label(screen, text = "",font=('trade gothic',15, 'bold'), bg = "#FFFFFF")
quote.place(x=qpx, y=qpy, width=320)


play = tk.PhotoImage(file="PL.ppm")
pause2 = tk.PhotoImage(file="PA.ppm")
violin = tk.PhotoImage(file="VI1.ppm")
violin2= tk.PhotoImage(file="VI2.ppm")
forward = tk.PhotoImage(file="FF1.ppm")
forward2 = tk.PhotoImage(file="FF2.ppm")
rewind = tk.PhotoImage(file="FW1.ppm")
rewind2 = tk.PhotoImage(file="FW2.ppm")
terrain = tk.PhotoImage(file="BI1.ppm")
terrain2 = tk.PhotoImage(file="BI2.ppm")



pauseplay = tk.Button(screen, command=pause, borderwidth = 0, highlightthickness = 0, bg = "#FFFFFF")
pauseplay.place(x=ppx, y=ppy)



notif = tk.Label(screen,font=('trade gothic',10, 'bold'), bg = "#FFFFFF")
notif.place(x=60, y=120, width=200)

yes = tk.Button(screen, command=yesmusic, text="yes", font=('arial',20, 'bold'), borderwidth = 0, highlightthickness = 0, bg = "#FFFFFF")
no = tk.Button(screen, command=nomusic, text="no", font=('arial',20, 'bold'), borderwidth = 0, highlightthickness = 0, bg = "#FFFFFF")

musiccontrol = tk.Frame(screen, width = 320, height = 3)
musiccontrol.config(background="#000000")

fastforward = tk.Button(screen, command=yesmusic, image=forward, borderwidth = 0, highlightthickness = 0, bg = "#FFFFFF")
rewindbutton = tk.Button(screen, command=yesmusic, image=rewind, borderwidth = 0, highlightthickness = 0, bg = "#FFFFFF")
currentmusic = tk.Button(screen, command=yesmusic, image=violin, borderwidth = 0, highlightthickness = 0, bg = "#FFFFFF")









#MUSIC

sound1 = sa.WaveObject.from_wave_file(os.path.join(os.getcwd(), "pause.wav"))
sound2 = sa.WaveObject.from_wave_file(os.path.join(os.getcwd(), "music", "bear_growl_y.wav"))
sound3 = sa.WaveObject.from_wave_file(os.path.join(os.getcwd(), "end.wav"))
music = sa.WaveObject.from_wave_file(os.path.join(os.getcwd(), "music", "bear_growl_y.wav"))








#EXPERIMENTAL




#REQUIRED
root.mainloop()
