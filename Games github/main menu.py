
import tkinter as tk
import subprocess
import sys
import os

def launch_game(folder_name, script_name, is_console_game=False):
    """
    Safely launches a game as an independent sub-process.
    Forces Windows CMD to open for console-based text games.
    """
    # Получаем абсолютный путь к папке, где лежит сам лаунчер
    base_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
    script_path = os.path.join(base_dir, folder_name, script_name)
    
    # Проверяем, существует ли файл игры по указанному пути
    if not os.path.exists(script_path):
        print(f"Error: Target game script not found at: {script_path}")
        return

    if is_console_game:
        # Для текстовых игр вызываем реальное окно cmd.exe. 
        # /K заставляет консоль остаться открытой после запуска, чтобы ты видел текст.
        # sys.executable гарантирует, что игра запустится на том же Python, что и лаунчер.
        subprocess.Popen(['cmd.exe', '/K', f'"{sys.executable}" "{script_path}"'])
    else:
        # Стандартный запуск для графических игр (Tkinter / Turtle)
        subprocess.Popen([sys.executable, script_path])

# Main Dashboard Architecture Initialization
window = tk.Tk()
window.geometry("380x180")
window.title("Python Retro Game Launcher")
window.configure(bg="#2c3e50")
window.resizable(False, False)

# Modern Title Heading
title_label = tk.Label(window, text="🕹️ RETRO GAME ARCHIVE 🕹️", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 12, "bold"))
title_label.pack(pady=10)

# Matrix layout frame container
button_frame = tk.Frame(window, bg="#2c3e50")
button_frame.pack()

# Row 1 Elements configuration (folder_name, script_name, is_console_game)
tk.Button(button_frame, text="Snake", width=13, 
          command=lambda: launch_game("snake", "snake.py")).grid(row=0, column=0, padx=4, pady=4)
tk.Button(button_frame, text="Colors", width=13, 
          command=lambda: launch_game("colors", "colors.py")).grid(row=0, column=1, padx=4, pady=4)
tk.Button(button_frame, text="Dice", width=13, 
          command=lambda: launch_game("dice", "dice.py", is_console_game=True)).grid(row=0, column=2, padx=4, pady=4)

# Row 2 Elements configuration
tk.Button(button_frame, text="Quest", width=13, 
          command=lambda: launch_game("quest", "quest.py", is_console_game=True)).grid(row=1, column=0, padx=4, pady=4)
tk.Button(button_frame, text="Tic Tac Toe", width=13, 
          command=lambda: launch_game("tictactoe", "tictactoe.py", is_console_game=True)).grid(row=1, column=1, padx=4, pady=4)
tk.Button(button_frame, text="Battleship", width=13, 
          command=lambda: launch_game("warship", "warship.py")).grid(row=1, column=2, padx=4, pady=4)

# Row 3 Elements configuration
tk.Button(button_frame, text="Wheel of Fortune", width=13, 
          command=lambda: launch_game("fieldofdreams", "fieldofdreams.py", is_console_game=True)).grid(row=2, column=0, padx=4, pady=4)
tk.Button(button_frame, text="Arrangement", width=13, 
          command=lambda: launch_game("arrangement", "arrangement.py")).grid(row=2, column=1, padx=4, pady=4)
tk.Button(button_frame, text="Guess Number", width=13, 
          command=lambda: launch_game("guesnumber", "guesnumber.py")).grid(row=2, column=2, padx=4, pady=4)

window.mainloop()
