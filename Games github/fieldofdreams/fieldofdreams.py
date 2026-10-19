
import random

# Game introduction
print("Welcome to the Wheel of Fortune game!")
print("Rules: Guess the hidden word letter by letter. Each correct guess adds points, each mistake costs points.")

name = input("Enter your name: ")
print(f"Good luck, {name}! Let's start the game.\n")

# Word bank for the game
words_pool = ["python", "developer", "programming", "github", "keyboard", "software"]
# Pick a random word from the pool
hidden_word = random.choice(words_pool)

# Create a masked word with underscores (e.g., "______")
guessed_letters = []
display_word = ["_"] * len(hidden_word)

points = 100

# Main game loop
while points > 0 and "_" in display_word:
    print(f"Current word: {' '.join(display_word)}")
    print(f"Your points: {points}")
    
    # Prompt user for a guess
    guess = input(f"Guess a letter, {name}: ").lower()
    
    # Validation check
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.\n")
        continue
        
    if guess in guessed_letters:
        print("You have already guessed this letter. Try another one.\n")
        continue
        
    guessed_letters.append(guess)
    
    # Check if the letter is in the hidden word
    if guess in hidden_word:
        print(f"Great job, {name}! Correct letter.")
        # Update the masked word display
        for index, letter in enumerate(hidden_word):
            if letter == guess:
                display_word[index] = guess
        points += 20  # Reward points for correct guess
    else:
        print(f"Sorry, {name}. The letter '{guess}' is not in the word.")
        points -= 15  # Deduct points for a mistake
    print("-" * 30)

# Game over conditions
if "_" not in display_word:
    print(f"Congratulations, {name}! You guessed the word: '{hidden_word}'!")
    print(f"Your final score is {points} points.")
else:
    print(f"Game over, {name}! You ran out of points.")
    print(f"The correct word was: '{hidden_word}'.")
