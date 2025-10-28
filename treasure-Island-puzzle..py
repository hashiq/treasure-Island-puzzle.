print("WELCOME TO TREASURE ISLAND")
user_name = input("what is your name player ?  :\n ")
user_choice = input("You are on cross-road :\n 'left' or 'right'\n ").lower()
option_list1 = ["left", "right"]
option_list2 = ["swim", "boat"]
option_list3 = ["yellow","red","blue"]
if user_choice in option_list1:
   if user_choice == "left":
      user_choice2 = input("You found a river, cross river by : ? \n 'swim' or 'boat'").lower()
      if user_choice2 in option_list2:
         if user_choice2 =="swim":
            user_choice3 = input("You found 3 doors to treasure: 'yellow','red' or 'blue' ").lower()
            if user_choice3 in option_list3:
              if user_choice3 =="red":
                 print(f"sorry {user_name}, it's a room full of beasts and you are dead")
              elif user_choice3 =="blue":
                  print(f"sorry {user_name}, it's a room full of fireballs and you are dead")
              elif user_choice3 =="yellow":
               print(f" {user_name}, You win!! ")
            else:
               print("Please enter a valid input")
         elif user_choice2 == "boat":
             print(f"sorry {user_name}, You died because of crocodile attack")
         else:
             print("Please enter a valid input ")
      else:
          print("Please enter a valid input")
   elif user_choice == "right":
    print(f"sorry {user_name}, You died , there is a quicksand-stream")
else:
    print("Please enter a valid input")






# else:
#     print("Please enter a valid input to continue the game")