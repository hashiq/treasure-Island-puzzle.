print("WELCOME TO TREASURE ISLAND")
user_name = input("what is your name player ?  :\n ")
user_choice = input("You found a cross-road what you wan to do:\n 'left' or 'right'\n ").lower()

if user_choice == "left":
    print("You escape the sand-stream and found a river ")
    user_choice2 = input("How you want to cross the river by : ? \n 'swim' or 'boat'").lower()
    if user_choice2 =="swim":
       print("You crossed the river , without any danger ")
       user_choice3 = input("you found the door to treasure, you have 3-doors: 'yellow','red' or 'blue' ").lower()
       if user_choice3 =="red":
            print(f"sorry {user_name}, it's a room full of beasts and you are dead")
       elif user_choice3 =="blue":
           print(f"sorry {user_name}, it's a room full of fireballs and you are dead")
       elif user_choice3 =="yellow":
            print(f" {user_name}, You got the hidden treasure ")
       else:
           print("Please enter a valid input to continue the game")
    elif user_choice2 == "boat":
        print(f"sorry {user_name}, You died because of crocodile attack")
    else:
        print("Please enter a valid input to continue the game")

elif user_choice == "right":
    print(f"sorry {user_name}, You died , there is a quicksand-stream")
else:
    print("Please enter a valid input to continue the game")






# else:
#     print("Please enter a valid input to continue the game")