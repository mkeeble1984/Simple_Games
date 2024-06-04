import random
r = random.randint(1, 10)
guess_counter = 0

print("""
Welcome to the number guessing game!!!!

I have randomly selected a number from 1 to 10, can you guess what it is??
            """)
while True:
    guess = input("Guess a number between 1 and 10 (including 1 and 10): ")
    guess_counter += 1

# Check if guess is a digit, then convert it to an integer
    if guess.isdigit():
        guess = int(guess)
        # Check if the number eneters is between 1 and 10
        if guess >= 0 and guess <= 10:
            print()
        else:
            print("""
    ERROR - Please eneter a number between 1 and 10 only.
                  """)
    else:
        print("""
    ERROR - Please type in a number.
              """)
    # Check if the guess is correct
    if guess < r:
        print("""     Too low, guess a higher number.
              """)
    elif guess > r:
        print("""     Too high, guess a lower number.
              """)
    else:
        print(f"""     Congratulations, you guessed correct!!!!
     It took you {guess_counter} attempts!!!
              """)
        break;

input("Press enter to quit. ")