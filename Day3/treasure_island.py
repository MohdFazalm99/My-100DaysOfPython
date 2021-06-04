print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island.") 
print(" Your Mission is to find the Treasue.")

choice1 = input('Which way do you want to go Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('Now what do want to choose? Do you want to "swim" or do you want to "wait".\n').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One "red", one "yellow" and one "blue. WHich door do you choose?\n').lower()
        if choice3 == "red":
            print("IT's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You win.")
        elif choice3 == "blue":
            print("You enter a room full of beasts. Game over")
        else:
            print("You choose a door that doesn't exit. Game over")

    else:
            print("You got attacked by an angry shark.. Game over ")
else:
    print( print("You fell into a hole.Game over..."))


