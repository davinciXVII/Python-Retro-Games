
import random as rnd
import tkinter as tk
import tkinter.messagebox as tkm

# Global variables for the game state
board_player = []
board_ai = []
player_buttons = {}
ai_buttons = {}
player_coords = []
button_done = None
player_points = 0
ai_points = 0

class Ship:
    def __init__(self, size=0):
        self.size = size
        self.coord = []
    def change_size(self):
        self.size = len(self.coord)
        return self.size

def end_game():
    # Remove click actions from AI board when game ends
    for coord in ai_buttons:
        ai_buttons[coord].configure(command=None)
    if ai_points == 20:
        tkm.showinfo("Game Over", "Computer Wins! Better luck next time.")
    else:
        tkm.showinfo("Victory!", "Congratulations! You won the Battleship game!")

def click_ai(coord):
    global player_points
    row, col = coord
    # 'K' represents a Ship cell (from Russian 'Корабль')
    if board_ai[row][col] == "К":
        player_points += 1
        ai_buttons[coord].configure(bg="red", command=None)
        if player_points == 20:
            end_game()
    else:
        ai_buttons[coord].configure(bg="light blue", command=None)
        if player_points < 20 and ai_points < 20:
            ai()

def ai():
    global ai_points
    if not player_coords or ai_points >= 20 or player_points >= 20:
        return
        
    rnd.shuffle(player_coords)
    shot = player_coords.pop()
    row, col = shot
    
    if board_player[row][col] == "К":
        ai_points += 1
        player_buttons[shot]["bg"] = "red"
        
        # Remove diagonal cells as ships cannot touch diagonally
        surroundings = [(row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]
        for coord in surroundings:
            if coord in player_coords:
                player_coords.remove(coord)
                
        if ai_points == 20:
            end_game()
        else:
            ai()  # AI shoots again on hit
    else:
        player_buttons[shot]["bg"] = "light blue"

def click_player(coord):
    global board_player
    row, col = coord
    color = player_buttons[coord].cget("bg")
    if color == "blue":
        player_buttons[coord].configure(bg="yellow")
        board_player[row][col] = "К"
    else:
        player_buttons[coord].configure(bg="blue")
        board_player[row][col] = ""

def diag(coord):
    row, col = coord
    return [(row+1, col-1), (row+1, col+1)] 
    
def sur(coord):
    row, col = coord
    return [(row-1, col), (row, col-1)]

def configuration():
    global ai_buttons, player_buttons, button_done, board_player
    ship_coords = []
    for row in range(10):
        for col in range(10):
            if board_player[row][col] == "К":
                ship_coords.append((row, col))
                
    for coord in ship_coords:
        for d_cord in diag(coord):
            if d_cord in ship_coords:
                tkm.showerror("Error", "Invalid Placement! Ships cannot touch diagonally.")
                return False
                
    my_ships = [Ship() for i in range(10)]
    try:
        for ship in my_ships:
            if not ship_coords:
                break
            ship.coord.append(ship_coords.pop())
            for i in range(4):
                up, left = sur(ship.coord[-1])
                if up in ship_coords:
                    ship_coords.remove(up)
                    if i == 3:
                        return False
                    ship.coord.append(up)
                if left in ship_coords:
                    ship_coords.remove(left)
                    if i == 3:
                        return False
                    ship.coord.append(left)
    except:
        print("Ship validation exception caught")
        
    ideal = {4: 1, 3: 2, 2: 3, 1: 4}
    reality = {}
    for ship in my_ships:
        size = ship.change_size()
        if size == 0:
            continue
        if size in reality:
            reality[size] += 1
        else:
            reality[size] = 1
            
    if reality == ideal:
        button_done.configure(state=tk.DISABLED)
        for coord in player_buttons:
            player_buttons[coord].configure(command=None)  # Lock player board after setup
        for coord in ai_buttons:
            ai_buttons[coord].configure(command=lambda c=coord: click_ai(c))
        tkm.showinfo("Success", "Fleet is ready! The battle begins. Attack the enemy board!")
    else:
        tkm.showwarning("Wrong Layout", "Your fleet must contain:\n1x 4-deck\n2x 3-deck\n3x 2-deck\n4x 1-deck ships!")

def create():
    global button_done, board_player, board_ai, ai_buttons, player_buttons, player_points, ai_points
    
    # Clear existing elements if restarting
    for child in window.winfo_children():
        if isinstance(child, tk.Button):
            child.destroy()
            
    button_done = tk.Button(window, text="Ready", font=("Arial", 10, "bold"), command=configuration)
    button_done.place(x=15 + 70*4 + 10, y=2, width=70, height=26)
    
    board_player = [["" for _ in range(10)] for _ in range(10)]
    board_ai = create_board_ai()
     
    player_points = 0
    ai_points = 0
    
    coordinates = [(i, j) for i in range(10) for j in range(10)]
    player_buttons.clear()
    ai_buttons.clear()
    
    for coord in coordinates:
        player_buttons[coord] = tk.Button(window, bg="blue", command=lambda c=coord: click_player(c))
        ai_buttons[coord] = tk.Button(window, bg="blue")
        
    for coord in coordinates:
        row, col = coord
        player_buttons[coord].place(height=35, width=35, x=10 + (col * 35), y=40 + (row * 35))
        ai_buttons[coord].place(height=35, width=35, x=450 + (col * 35), y=40 + (row * 35))

def full_sur(coord):
    row, col = coord
    return [[row-1, col-1], [row-1, col], [row-1, col+1], 
            [row, col-1],                 [row, col+1], 
            [row+1, col-1], [row+1, col], [row+1, col+1]]

def create_board_ai():
    global player_coords
    ai_ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    coords = [[i, j] for i in range(10) for j in range(10)]
    player_coords = [(i, j) for i in range(10) for j in range(10)]
    b_ai = [["" for _ in range(10)] for _ in range(10)]
    
    for ship in ai_ships:
        done = False
        attempts = 0
        while not done and attempts < 200:
            attempts += 1
            start_cell = rnd.choice(coords)
            row, col = start_cell
            if rnd.randint(0, 1):
                ship_coords = [[row+i, col] for i in range(ship)]
            else:
                ship_coords = [[row, col+i] for i in range(ship)]
                
            good_ship = True
            for coord in ship_coords:
                if coord not in coords:
                    good_ship = False
            if good_ship:
                done = True
                
        if not done:
            return create_board_ai()  # Recalculate if generator gets stuck
            
        for coord in ship_coords:
            coords.remove(coord)
        for coord in ship_coords:
            for s_coord in full_sur(coord):
                if s_coord in coords:
                    coords.remove(s_coord)
        for coord in ship_coords:
            row, col = coord
            b_ai[row][col] = "К"
    return b_ai

def new_game():
    answer = tkm.askokcancel("New Game", "Are you sure you want to restart? Current game progress will be lost.")
    if answer:
        create()

def leave():
    answer = tkm.askokcancel("Exit", "Are you sure you want to quit the game?")
    if answer:
        window.destroy()

# Main Program Initialization
window = tk.Tk()
window.title("Battleship Game")
window.geometry("820x410")
window.resizable(False, False)

create()

# Game Menu bar
main_menu = tk.Menu(window)
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label="New Game", command=new_game)
file_menu.add_command(label="Exit", command=leave)

main_menu.add_cascade(label="Game", menu=file_menu)
window.configure(menu=main_menu)

window.mainloop()
