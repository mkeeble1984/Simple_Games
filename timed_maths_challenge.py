import random
import os
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

repeat = "Y"
choice = ""

while repeat == "Y":
    EASY_OPERATORS = ["+"]
    TOTAL_PROBLEMS_E = 5
    MID_OPERATORS = ["+", "-"]
    TOTAL_PROBLEMS_M = 10
    HARD_OPERATORS = ["+", "-", "*"]
    TOTAL_PROBLEMS_H = 15
    MIN_OPERAND = 3
    MAX_OPERAND = 12

    while choice != "E" or choice != "M" or choice != "H":
        os.system("cls")
        print(Fore.LIGHTBLUE_EX,"""Welcome to the Timed Maths Challenge!!!
 You will be given a series of maths questions to answer, and timed on how quickly you can get them correct.""")

        choice = input("\n Would you like to play the Easy, Moderate or Hard game? (E / M / H): ").upper()
        print("")
        wrong = 0
        confirm = ""

        if choice == "R":
            while confirm != "Y" or confirm != "N":
                print(Fore.RED)
                confirm = input("Are you sure you want to reset all top scores? (Y / N): ").upper()
                if confirm == "Y":
                    print(Fore.LIGHTGREEN_EX,"\nAll top scores have been reset to 100.00 seconds.")
                    with open ("C:\\Users\mkeeb\OneDrive\Documents\Matt\Programming\Simple Games\Timed Maths Challenge Top Scores\easy_top_scores.txt", "w") as file:
                        file.write("100.00")
                        file.close()
                        pass
                    with open ("C:\\Users\mkeeb\OneDrive\Documents\Matt\Programming\Simple Games\Timed Maths Challenge Top Scores\mid_top_scores.txt", "w") as file:
                        file.write("100.00")
                        file.close()
                        pass
                    with open ("C:\\Users\mkeeb\OneDrive\Documents\Matt\Programming\Simple Games\Timed Maths Challenge Top Scores\hard_top_scores.txt", "w") as file:
                        file.write("100.00")
                        file.close()
                        pass
                    time.sleep(4)
                    break
                elif confirm == "N":
                    break
                else:
                    print(Fore.LIGHTRED_EX,"\nPlease eneter a valid choice. (Y / N)")
                    time.sleep(4)
                    os.system("cls")
   
        elif choice == "E":
            with open ("C:\\Users\mkeeb\OneDrive\Documents\Matt\Programming\Simple Games\Timed Maths Challenge Top Scores\easy_top_scores.txt", "r") as file:
                easy_top_score = file.read()

            print(Fore.YELLOW,f"The top score for easy mode is {easy_top_score} seconds.")
            input(" Press enter to start!")
            print(Fore.RESET,"\n---------------------\n")

            start_time = time.time()

            def generate_problem():
                left = random.randint(MIN_OPERAND, MAX_OPERAND)
                right = random.randint(MIN_OPERAND, MAX_OPERAND)
                operator = random.choice(EASY_OPERATORS)

                sum = str(left) + " " + operator + " " + str(right)
                answer = eval(sum)
                return sum, answer
            for i in range(TOTAL_PROBLEMS_E):
                sum, answer = generate_problem()
                while True:
                    guess = input(f"Question No.{str(i + 1)}: {sum}: ")
                    if guess == str(answer):
                       break
                    else:
                        print("WRONG - Guess again!\n")
                        wrong += 1

            break
        elif choice == "M":
            with open ("C:\\Users\mkeeb\OneDrive\Documents\Matt\Programming\Simple Games\Timed Maths Challenge Top Scores\mid_top_scores.txt", "r") as file:
                easy_top_score = file.read()

            print(Fore.YELLOW,f"The top score for moderate mode is {easy_top_score} seconds.")

            input(" Press enter to start!")
            print(Fore.RESET,"\n---------------------\n")
            start_time = time.time()

            def generate_problem():
                left = random.randint(MIN_OPERAND, MAX_OPERAND)
                right = random.randint(MIN_OPERAND, MAX_OPERAND)
                operator = random.choice(MID_OPERATORS)

                sum = str(left) + " " + operator + " " + str(right)
                answer = eval(sum)
                return sum, answer

            for i in range(TOTAL_PROBLEMS_M):
                sum, answer = generate_problem()
                while True:
                    guess = input(f"Question No.{str(i + 1)}: {sum}: ")
                    if guess == str(answer):
                        break
                    else:
                        print("WRONG - Guess again!\n")
                        wrong += 1
                        
            break
        elif choice == "H":
            with open ("C:\\Users\mkeeb\OneDrive\Documents\Matt\Programming\Simple Games\Timed Maths Challenge Top Scores\hard_top_scores.txt", "r") as file:
                easy_top_score = file.read()

            print(Fore.YELLOW,f"The top score for hard mode is {easy_top_score} seconds.")

            input(" Press enter to start!")
            print(Fore.RESET,"\n---------------------\n")
            start_time = time.time()

            def generate_problem():
                left = random.randint(MIN_OPERAND, MAX_OPERAND)
                right = random.randint(MIN_OPERAND, MAX_OPERAND)
                operator = random.choice(HARD_OPERATORS)

                sum = str(left) + " " + operator + " " + str(right)
                answer = eval(sum)
                return sum, answer

            for i in range(TOTAL_PROBLEMS_H):
                sum, answer = generate_problem()
                while True:
                    guess = input(f"Question No.{str(i + 1)}: {sum}: ")
                    if guess == str(answer):
                        break
                    else:
                        print("WRONG - Guess again!\n")
                        wrong += 1

            break
        else:
            print(Fore.LIGHTRED_EX,"\nPlease eneter a valid choice. (E / M / H)")
            time.sleep(4)
            os.system("cls")

    print("\n---------------------\n")
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    total_time = str(total_time)
    print(Fore.LIGHTYELLOW_EX,f"Well done!!! You finished in {total_time} seconds. You made {wrong} mistakes.")

    if total_time > easy_top_score:
        print(Fore.YELLOW,"You have set a new top score!!!")
        if choice == "E":
            with open ("C:\\Users\mkeeb\OneDrive\Documents\Matt\Programming\Simple Games\Timed Maths Challenge Top Scores\easy_top_scores.txt", "w") as file:
                file.write(total_time)
                file.close()
                pass
        elif choice == "M":
            with open ("C:\\Users\mkeeb\OneDrive\Documents\Matt\Programming\Simple Games\Timed Maths Challenge Top Scores\mid_top_scores.txt", "w") as file:
                file.write(total_time)
                file.close()
                pass
        elif choice == "H":
            with open ("C:\\Users\mkeeb\OneDrive\Documents\Matt\Programming\Simple Games\Timed Maths Challenge Top Scores\hard_top_scores.txt", "w") as file:
                file.write(total_time)
                file.close()
                pass
        else:
            break

    while repeat != "Y" or repeat != "N":
        print(Fore.RESET)
        repeat = input("Would you like to play again? (Y / N): ").upper()
        if repeat == "Y":
            break
        elif repeat == "N":
            break
        else:
            print(Fore.LIGHTRED_EX,"\nPlease eneter a valid choice. (Y / N)")
            time.sleep(4)
            os.system("cls")