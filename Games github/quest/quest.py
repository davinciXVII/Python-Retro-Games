
        # Text-Based Quest: Room Escape Game
inventory = []

def check_item(name):
    """Safely checks if an item exists in the player's inventory."""
    return name in inventory

def bedroom():
    print("\n=== BEDROOM ===")
    print("You are in a minimally decorated bedroom. There is a bed, a nightstand, a window, and a door.")
    print("What do you want to do?")
    print("1. Open the window")
    print("2. Go through the door")
    print("3. Open the nightstand")
    
    answer = input("Your choice: ")
    print("-" * 40)
    
    if answer == "1":
        print("You opened the window. You see that the room is on the 20th floor.")
        bedroom()
    elif answer == "2":
        print("You walked out into the corridor.")
        corridor()
    elif answer == "3":
        if check_item("key"):
            print("You have already searched the nightstand. It's empty.")
        else:
            print("Inside the nightstand, you found a KEY!")
            inventory.append("key")
        bedroom()
    else:
        print("Command not recognized.")
        bedroom()

def corridor():
    print("\n=== CORRIDOR ===")
    print("You are in a long, dark corridor with 5 doors.")
    print("1. Open the exit door to the street")
    print("2. Open the door to the Living Room")
    print("3. Open the door to the Mystery Room")
    print("4. Go back to the Bedroom")
    print("5. Go to the Kitchen")
    
    answer = input("Your choice: ")
    print("-" * 40)
    
    if answer == "1":
        print("You tried to open the exit door, but it is heavily barricaded with wooden boards.")
        corridor()
    elif answer == "2":
        print("You opened the door to the living room.")
        livingroom()
    elif answer == "3":
        print("You opened the door to the mystery room.")
        room()
    elif answer == "4":
        print("You returned to the starting location.")
        bedroom()
    elif answer == "5":
        print("You walked into the kitchen.")
        kitchen()
    else:
        print("Command not recognized.")
        corridor()
        
def livingroom():
    print("\n=== LIVING ROOM ===")
    print("There is an old TV and a sofa here.")
    print("1. Look behind the sofa")
    print("2. Look under the sofa")
    print("3. Look behind the TV")
    print("4. Go back to the Corridor")
    
    answer = input("Your choice: ")
    print("-" * 40)
    
    if answer == "1":
        print("Behind the sofa is full of dust. You found nothing.")
        livingroom()
    elif answer == "2":
        if check_item("note"):
            print("You already have the note. It reads: 'LOOK BEHIND THE TV!'")
        else:
            print("You peeked under the sofa and found a NOTE!")
            print("The note reads: 'LOOK BEHIND THE TV!'")
            inventory.append("note")
        livingroom()
    elif answer == "3":
        if check_item("flashlight"):
            print("There is nothing else behind the TV.")
        else:
            print("You found a FLASHLIGHT behind the TV!")
            inventory.append("flashlight")
        livingroom()
    elif answer == "4":
        corridor()
    else:
        print("Command not recognized.")
        livingroom()
        
def room():
    print("\n=== MYSTERY ROOM ===")
    print("This room is unusual. There is a wardrobe, a desk with a vase on it, and a locked chest.")
    print("1. Open the wardrobe")
    print("2. Look inside the vase")
    print("3. Open the chest")
    print("4. Go back to the Corridor")
    
    answer = input("Your choice: ")
    print("-" * 40)
    
    if answer == "1":
        if check_item("key_2"):
            print("The wardrobe is completely empty now.")
        else:
            print("You opened the wardrobe. It looks empty, but you checked the top shelf and found a spare KEY!")
            inventory.append("key_2")
        room()
    elif answer == "2":
        if check_item("powder"):
            print("The vase is empty now.")
        else:
            print("You found a strange toxic powder inside the vase and picked it up.")
            inventory.append("powder")
        room()
    elif answer == "3":
        print("The chest is wrapped tightly in heavy iron chains.")
        if check_item("key") or check_item("key_2"):
            if check_item("bunch of keys"):
                print("You have already opened the chest.")
            else:
                print("You used the key on the chains. It fits perfectly! Inside the chest, you found a BUNCH OF KEYS!")
                inventory.append("bunch of keys")
        else:
            print("You need a key to open these chains.")
        room()
    elif answer == "4":
        corridor()
    else:
        print("Command not recognized.")
        room()

def kitchen():
    print("\n=== KITCHEN ===")
    print("You entered the kitchen. You notice that the safe is here.")
    
    # Safe interaction logic sequence
    if check_item("bunch of keys"):
        print("You used your bunch of keys to unlock the safe!")
        if not check_item("knife"):
            print("Inside the safe, you found a sharp KNIFE!")
            inventory.append("knife")
    else:
        print("There is a safe on the table, but it is securely locked.")
        
    print("\nYou also notice that the window is wide open and there is an escape ladder outside!")
    print("1. Try to escape through the window")
    print("2. Stay in the kitchen")
    
    answer = input("Your choice: ")
    print("-" * 40)
    
    if answer == "1":
        print("You decided to make a run for it! You rushed to the window and climbed onto the ladder.")
        print("You climbed down safely and reached the ground.")
        print("\n🎉 YOU ESCAPED! YOU WIN! 🎉")
    elif answer == "2":
        print("You decided to stay... Suddenly, a monster appeared behind you!")
        print("\n💀 YOU WERE KILLED! GAME OVER 💀")
    else:
        print("Command not recognized.")
        kitchen()

# Start the game environment
if __name__ == "__main__":
    print("🤖 Welcome to the Escape Room Text RPG! 🤖")
    bedroom()

                
                
                
        
            
            

        
    
  
            

            
        
        
    
    
            
            
    
    
    
        

        
        
    
