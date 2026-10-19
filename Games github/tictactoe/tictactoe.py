# Render the game board. Allow placing X and O on the board.
# Simple Artificial Intelligence included. The program detects win conditions.
import random as rnd

board = [["", 1, 2, 3], [1, "*", "*", "*"], [2, "*", "*", "*"], [3, "*", "*", "*"]]

def display():
    for row in board:
        for sim in row:
            print(sim, end="\t")
        print()

def game():
    cont = True
    while True:
        print()
        display()
        print()
        print("Where do you want to place X?\nRow number - Column number (e.g., 1-1)")
        answer = input()
        row, col = int(answer[0]), int(answer[-1])
        if board[row][col] == "*":
            board[row][col] = "X"
            break
        else:
            print("This cell is already taken. Try again.")
        
    if win("X"):
        display()
        print("X Wins!")
        cont = False
    if cont:
        ai()
    if win("O"):
        display()
        print("O Wins!")
        cont = False
    if cont:
        game()
    else:
        another_try()

def win(player):
    d1 = 0
    d2 = 0
    for i in range(4):
        row = 0
        col = 0
        for j in range(4):
            if board[i][j] == player:
                row += 1
            if board[j][i] == player:
                col += 1
            if board[i][j] == player and i == j:
                d1 += 1
            if board[i][j] == player and i + j == 4:
                d2 += 1
        if row == 3 or col == 3 or d1 == 3 or d2 == 3:
            return True
    return False

def ai():
    if board[2][2] == "*":
        board[2][2] = "O"
        return True
    answers = []
    for row, cont in enumerate(board):
        for col, sim in enumerate(cont):
            if sim == "*":
                answers.append([row, col])
    winning = []
    loosing = []
    for answer in answers:
        row = answer[0]
        col = answer[1]
        board[row][col] = "O"
        if win("O"):
            winning.append(answer)
        board[row][col] = "X"
        if win("X"):
            loosing.append(answer)
        board[row][col] = "*"
        
    if winning:
        row, col = rnd.choice(winning)
    elif loosing:
        row, col = rnd.choice(loosing)
    else:
        row, col = rnd.choice(answers)
    board[row][col] = "O"

def another_try():
    # Prompt the player to restart the game after a win condition.
    # If the answer is "yes", the game resets.
    answer = input("Do you want to play again? (yes/no): ").lower()
    if answer == "yes":
        global board
        # Resetting the board state for a new game
        board = [["", 1, 2, 3], [1, "*", "*", "*"], [2, "*", "*", "*"], [3, "*", "*", "*"]]
        print("The game has restarted!")
        game()
        
game()
    
    
