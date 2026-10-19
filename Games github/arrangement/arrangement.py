import random as rnd
import tkinter as tk
from tkinter import messagebox  # Used for the neat win condition popup

# Global variables
board = []
buttons = {}
side = 0

def check_win():
    # Win condition logic: numbers must be in ascending order (1, 2, 3...)
    # and the empty cell "" must be at the very bottom-right corner.
    expected_value = 1
    for i in range(1, side + 1):
        for j in range(1, side + 1):
            # Check if the bottom-right corner is empty
            if i == side and j == side:
                if board[i][j] != "":
                    return False
            else:
                if board[i][j] != expected_value:
                    return False
                expected_value += 1
                
    # If the loop finishes without returning False, the player wins!
    messagebox.showinfo("Congratulations!", "You Win!")
    window.destroy()  # Close the game window after victory

def display():
    for row, col in buttons:
        buttons[(row, col)].configure(text=board[row][col])
 
def get_coordinates(row, col):
    # Check adjacent cells (up, down, left, right)
    list_of_cord = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]
    for cord in list_of_cord:
        temp_row = cord[0]
        temp_col = cord[1]
        # Ensure we don't go out of the board boundaries and the cell is empty
        if 0 <= temp_row < len(board) and 0 <= temp_col < len(board):
            if board[temp_row][temp_col] == "":
                return temp_row, temp_col
    return None, None
    
def click(row, col):
    n_row, n_col = get_coordinates(row, col)
    # Fixed the zero-index bug by checking if coordinates are not None
    if n_row is not None:
        board[n_row][n_col] = board[row][col]
        board[row][col] = ""
        display()
        check_win()

def create_click(cord):
    return lambda: click(cord[0], cord[1])

def start():
    window.title("Sliding Puzzle")
    window.geometry("250x120")
    
    global msg, entr, btn
    msg = tk.Label(window, text="Enter board size (e.g., 3 for 3x3):")
    msg.place(x=10, y=10)
    
    entr = tk.Entry(window)
    entr.place(x=10, y=40)
    
    btn = tk.Button(window, text="Create Game", command=create)
    btn.place(x=10, y=70)

def create():
    global board, side, buttons
    try:
        side = int(entr.get())
    except:
        msg["text"] = "Please enter a valid number!"
        return
        
    # Generate puzzle tiles (numbers from 1 to side^2 - 1) and one empty space
    pieces = [i for i in range(1, side**2)]
    pieces.append("")
    rnd.shuffle(pieces)
    
    # Initialize the board with outer borders ("!" and "1")
    board = []
    for _ in range(side + 2):
        board.append([])
        
    for i in range(side + 2):
        for j in range(side + 2):
            if i == 0 or i == side + 1:
                board[i].append("!")
            elif j == 0 or j == side + 1:
                board[i].append("1")
            else:
                board[i].append(pieces.pop())
    
    # Resize UI window to match the generated board size dynamically
    window.geometry(f"{side * 100}x{side * 100}")
    msg.destroy()
    btn.destroy()
    entr.destroy()
    
    cord = [(i, j) for i in range(1, side + 1) for j in range(1, side + 1)]
    buttons = {i: tk.Button(window, bg="black", fg="green", font=("Arial", 20, "bold"), command=create_click(i)) for i in cord}

    for row, col in buttons:
        y = (row - 1) * 100
        x = (col - 1) * 100
        buttons[(row, col)].place(x=x, y=y, height=100, width=100)
        
    display()  

window = tk.Tk()
start()
window.mainloop()
    

