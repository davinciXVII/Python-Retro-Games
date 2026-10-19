import tkinter as tk
import random as rnd
from tkinter import *
import tkinter.font as tkfont
#import tkinter.messagebox as tkm




def new_word():
    color.configure(fg=rnd.choice(colors),text=rnd.choice(colors))

def check(event):
    global score,fails
    global timer
   
    
    
    original_color=color["fg"]
    user_color=entry.get()
    entry.delete(0,"end")
    if original_color==user_color:
        print("yes")
        score=score+1
        win_label.configure(text=f"score={score}")
    else:
        print("no")
        fails=fails+1
        fail_label.configure(text=f"fail={fails}")
    new_word()

def countdown():
    global timer,score,fails
    if timer>0:
        timer=timer-1
        timer_label.configure(text=f"time left={timer}")
        timer_label.after(1000,countdown)
    else:
        window2=tk.Tk()
        window2.geometry("150x100")
        statemant=tk.Label(window2)
        statemant.place(x=10,y=10)
        if score>fails:
            statemant["text"]="you win"
        elif score<fails:
            statemant["text"]="you lose"
        else:
            statemant["text"]="draw"
            
        
        
    

#when the timer reaches 0, display a message indicating whether we won or lost; 
        #if we have more incorrect answers, display "you lost"
    
window=tk.Tk()
window.title("colors")
window.geometry("350x250")
window.bind("<Return>",check)

instructions=tk.Label(window,text="Enter the color of the word press enter to play")
instructions.place(x=10,y=10)
colorfont=tkfont.Font(size=60)
color=tk.Label(window,text="color",font=colorfont)
color.place(x=10,y=80)
entry=tk.Entry(window)
entry.place(x=10,y=180)
entry.focus_set()
colors = ["red", "blue", "green", "pink", "black", "yellow", "orange", "purple", "brown", "white"]

new_word()
score=0
win_label=tk.Label(window,text=f"score={score}")
win_label.place(x=10,y=40)
fails=0
fail_label=tk.Label(window,text=f"fail={fails}")
fail_label.place(x=10,y=60)
timer=30
timer_label=tk.Label(window,text=f"time left={timer}")
timer_label.place(x=10,y=210)
timer_label.after(1000,countdown)
window.mainloop()
