
import tkinter as tk
import random as rnd


def check():
    global attempts
    global number
    usernumber = entry.get()
    try:
        usernumber = int(usernumber)
    except:
        print("Please enter a valid number")
        return
    entry.delete(0, "end")
    if attempts > 0:
        attempts -= 1
        attempts_label["text"] = f"Attempts left: {attempts}"
        
       
        if number < usernumber:
            label["text"] = "Too high! Try a lower number."
        elif number > usernumber:
            label["text"] = "Too low! Try a higher number."
        else:
            label["text"] = "You guessed it! You win!"
            gues_button.configure(state=tk.DISABLED)
            reset_button.configure(state=tk.NORMAL)
            
        if attempts == 0 and number != usernumber:
            label["text"] = f"Game over! The number was {number}"
            gues_button.configure(state=tk.DISABLED)
            reset_button.configure(state=tk.NORMAL)


def reset():
    global attempts
    global number
    number = rnd.randint(1, 100)
    attempts = 10
    label["text"] = "Guess a number from 1 to 100"
    gues_button.configure(state=tk.NORMAL)
    reset_button.configure(state=tk.DISABLED)
    attempts_label["text"] = f"Attempts left: {attempts}"
    
    
# Create a reset function that generates a new number, resets
# the number of attempts, and binds it to the reset button.
    

window = tk.Tk()
window.geometry("200x150")
window.title("Guess the Number")
number = rnd.randint(1, 100)

label = tk.Label(window, text="Guess a number from 1 to 100")
label.place(x=30, y=10)

attempts = 10
attempts_label = tk.Label(window, text=f"Attempts left: {attempts}")
attempts_label.place(x=30, y=30)

entry = tk.Entry(window)
entry.place(x=30, y=50)
entry.focus_set()

gues_button = tk.Button(window, text="Check", width=17, command=check)
gues_button.place(x=30, y=80)

reset_button = tk.Button(window, text="Play Again", width=17, state=tk.DISABLED, command=reset)
reset_button.place(x=30, y=110)

window.mainloop()
