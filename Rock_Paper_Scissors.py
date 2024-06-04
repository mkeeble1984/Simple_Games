import random

user_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]

print("Welcome to Matt's amazing Rock - Paper - Scissors game!!!!")

while True:
    user_input = input("""
Rock[R] - Paper[P] - Scissors[S] (or Q to quit the game) --  Make your choice! > """).lower()
    
    if user_input == "q":
        print("""
              Fair enough, hopefully we can play again soon!!""")
        input("              Press enter to quit.")
        quit();
    
    elif user_input == "r":
        user_input = "rock"
    elif user_input == "p":
        user_input = "paper"
    elif user_input == "s":
        user_input = "scissors"
    
    elif user_input not in choices:
        print("""
              ERROR - You must choose either Rock, Paper or Scissors!""")
        continue
    
    random_number = random.randint(0, 2)
    computer_choice = choices[random_number]
    print(f"""
          Computer chose {computer_choice}.""")
    
    if user_input == computer_choice:
        print("""
              It's a draw, no-one wins.""")
        print(f"        Score -- Computer {computer_wins} / {user_wins} Player")

        continue;
    
    if user_input == "rock" and computer_choice == "scissors":
        print("""
              You win!!""")
        user_wins += 1
        print(f"        Score -- Computer {computer_wins} / {user_wins} Player")
            
    elif user_input == "paper" and computer_choice == "rock":
        print("""
              You win!!""")
        user_wins += 1
        print(f"        Score -- Computer {computer_wins} / {user_wins} Player")
            
    elif user_input == "scissors" and computer_choice == "paper":
        print("""
              You win!!""")
        user_wins += 1
        print(f"        Score -- Computer {computer_wins} / {user_wins} Player")
        
    else:
        print("""
              You lose.""")
        computer_wins += 1
        print(f"        Score -- Computer {computer_wins} / {user_wins} Player")
