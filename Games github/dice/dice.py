import random

print("Choose a number from 2 to 12. If the dice total is less than 7 and your chosen number is also less than 7, you win the bet. Likewise, if both are greater than 7, you win. If you guess the exact total, your bet is multiplied by 4!")

name = "Dawid"
name = input("Enter your name: ")
print("Now I know your name is " + name)

points = 100
# The number list variable is initialized but not directly used in the loop logic
number = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while points > 0:
    number = int(input(f"Choose a number, {name}: "))
    if number < 2 or number > 12:
        print("Wrong number, " + name)
        continue
        
    bet = int(input("Place your bet, " + name + ": "))
    if bet > points:
        print("You cannot bet this much, " + name)
        continue
        
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_total = dice_1 + dice_2
    print(f"The dice rolled: {dice_1} and {dice_2} (Total: {dice_total}), {name}")
    
    if number == dice_total:
        print(f"You win {bet * 4}! " + name)
        print(f"You have {bet * 4 + points} points, " + name)
        points = points + (bet * 4)
    elif number < 7 and dice_total < 7:
        print(f"You win {bet}! " + name)
        print(f"You have {bet + points} points, " + name)
        points = points + bet
    elif number > 7 and dice_total > 7:
        print(f"You win {bet}! " + name)
        print(f"You have {bet + points} points, " + name)
        points = points + bet
    else:
        print("You lose, " + name)
        print(f"You have {points - bet} points, " + name)
        points = points - bet

    answer = input("Do you want to continue? (yes/no) " + name + ": ").lower()
    if answer == "no":
        print("Game stopped, " + name)
        break

if points == 0:
    print("You lost the game! Out of points, " + name)

    



   
