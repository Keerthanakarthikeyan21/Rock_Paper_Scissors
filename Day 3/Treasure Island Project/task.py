print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("The treasure is inside the dangerous thick forest!")
print("Get ready for the adventure!")
direction = input("Now you are at the cross road! Where do you want to go?\n  Type left or right?\n ").lower()
if direction == "right":
    print("Oops! You was eaten by a lion")
    print("Better luck next time!")
elif direction == "left":
    print("You arrived at the lake! There is an island in the middle of the lake")
    decision = input("type 'wait' to wait for a boat or type 'swim' to swim across\n ").lower()
    if decision == "swim":
        print("OMG! You are surrounded by snakes and crocodiles! \n You lost the game\n Game Over!")
    elif decision == "wait":
        print("You have arrived the island safely! There is a hut here, in that there are 3 doors, red, blue and yellow")
        door_color = input("Which door you wanna choose? red or blue or yellow? ").lower()
        if door_color == "yellow":
            print("Hurrayyyyyy You won the treasure!")
            print("Congratulations!!!")
        elif door_color == "red":
            print("You got burned in the fire")
            print(":( You lost the treasure!")
        elif door_color == "blue":
            print("You got eaten by a monster!")
            print("Better luck next time")
        else:
            print("You choose something which doesn't exist")
    else:
        print("You choose something which doesn't exist!")
else:
    print("You choose something which doesn't exist!")


