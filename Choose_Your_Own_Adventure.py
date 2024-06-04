# Into
print("""
Welcome to 'The Most Amazing Adventure Game'!!!
Throughout this adventure you will be faced with a number of choices. 
Each choice will determine your fate, so choose wisely!!""")

# Do you want to begin and name enter
while True:
    begin_choice = input("""
                     Do you want to begin? (Y/N) > """).lower()
    if begin_choice == "y" or begin_choice == "yes":
        print("""
Great!""")
        player_name = input("What is your name? > ")
        player_name = player_name.capitalize()
        break;
    elif begin_choice == "n" or begin_choice == "no":
        print("""
You wuss!!! OK, some other time then. Press enter to quit.""")
        input()
        quit()
    else:
        print("""
-----------------------------              
ERROR - Answer must be Y or N.
-----------------------------              
              """)

print(f"""
Welcome {player_name}. 

If you want to leave the adventure at any time, simply type in 'Q' for quit.

Let's begin!""")
# Start of the adventure
answer = input("""
The day started like any other day, the sun was shining and the birds were chirping in the trees.
You decide to go for a walk. After putting on a nice hat and some comfortable shoes, you set off.
As you walk you come to a fork in the road, do you want to go right or left? (R/L) > """).lower()
# Q1 - right
if answer == "r" or answer == "right":
    answer = input(f"""
The fork on the right continues for many miles. The sun continues to beat down and you can feel youself getting hotter and hotter.
You are sweating more and more. It is time to take a drink. But {player_name}, did you remember your water bottle? (Y/N) > """).lower()
    if answer == "q" or answer == "quit":
        print("""
Thank you for playing, I hope you had fun. Press enter to quit""")
        input()
        quit()
    elif answer == "n" or answer == "no":
        answer = input("""
Oh no!!!! Without water, you will become dehydrated and die! 
Luckily in the distance you can see a shop. You are saved!!!!
Behind the counter is a grumpy old man. He gives you an evil look when you enter.
The shelves are bare, except for a mouldy loaf of bread and some questionable milk.
You spot two bottles of water on a shelf, one still and one sparkling.
Which do you choose? Still (St) or sparkling (Sp)? > """)
        if answer == "q" or answer == "quit":
            print("""
Thank you for playing, I hope you had fun. Press enter to quit""")
            input()
            quit()
        elif answer == "st" or answer == "still":
            answer = input("You chose still.")
            # Need a next step
        elif answer == "sp" or answer == "sparkling":
            answer = input("You chose sparkling.")
            # Need a next step
        else:
            print("""
-----------------------------------              
ERROR - Invalid answer - Game over.
-----------------------------------              
              """)
            input()
            quit()
    elif answer == "y" or answer == "yes":
        answer = input("Luck favours the prepared!")
            # Need to add in next choice
    else:
        print("""
-----------------------------------              
ERROR - Invalid answer - Game over.
-----------------------------------              
              """)
        input()
        quit()
# Q1 - left
elif answer == "l" or answer == "left":
    answer = input("""
After taking the left fork you quickly come across a wide river with a bridge over it. 
The river is shallow but flowing pretty quick and it looks dangerous. You are so hot and it would feel nice to dip your feet in.
The bridge is very old and in need of some repair, could this be a better way to cross the river?
Which path do you take? Wade through the river or cross the bridge? (R/B) > """).lower()
    if answer == "q" or answer == "quit":
        print("""
Thank you for playing, I hope you had fun. Press enter to quit""")
        answer = input()
        quit()
    elif answer == "r" or answer == "river":
        answer = input(f"""
The water feels great on your feet and is really cooling you down. 
As you continue to wade towards the middle the current seems to be getting faster and faster.
You loose your footing and slip, drenching your entire body with cold water.
{player_name}, what are you going to do now? 
It's quite sunny, if you keep going, maybe you will dry off?
Alternatively, you can turn back now and head home. Keep going (K) or turn back (T)? > """)
        if answer == "q" or answer == "quit":
            print("""
Thank you for playing, I hope you had fun. Press enter to quit""")
            input()
            quit()
        elif answer == "k" or answer == "keep going":
            answer = input("You chose to keep going.")
            # Need a new branch
        elif answer == "t" or answer == "turn back":
            answer = input(f"""
You chose to turn back and go home. Are you done with the story already {player_name}?
Oh well, if that's what you want.
Feel free to play again any time.""")
            quit()
        else:
            print("""
-----------------------------------              
ERROR - Invalid answer - Game over.
-----------------------------------              
              """)
            input()
            quit()
    elif answer == "b" or answer == "bridge":
        print("You took the bridge.")
        input()
            # Need to add in next choice
    else:
        print("""
-----------------------------------              
ERROR - Invalid answer - Game over.
-----------------------------------              
              """)
        input()
        quit()
elif answer == "q" or answer == "quit":
        print("""
Thank you for playing, I hope you had fun. Press enter to quit""")
        input()
        quit()
else:
    print("""
-----------------------------------              
ERROR - Invalid answer - Game over.
-----------------------------------              
              """)
    input()
    quit()
