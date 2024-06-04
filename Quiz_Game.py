# Intro
print("""
Welcome to Matt's Amazing Quiz!!!!!!

      """)
# Ready to play loop
while True:
    playing = input("Are you ready to play? (Y/N): ")
    if playing.lower() == "y":
        print("Great, let's begin.")
        break;
    elif playing.lower() == "n":
        print("OK, maybe next time.")
        quit()
    else:
        print("""
-----------------------------              
ERROR - Input must be Y or N.
-----------------------------              
              """)
# Questions
score = 0
answer = input("""
1. What does CPU stand for? """)
if answer.lower() == "central processing unit":
    print("Correct!  😄")
    score += 1
else:
    print("Incorrect  😞")

print(f"Your score so far is {score} / 5.")

answer = input("""
2. What does GPU stand for? """)
if answer.lower() == "graphics processing unit":
    print("Correct!  😄")
    score += 1
else:
    print("Incorrect  😞")

print(f"Your score so far is {score} / 5.")

answer = input("""
3. What does RAM stand for? """)
if answer.lower() == "random access memory":
    print("Correct!  😄")
    score += 1
else:
    print("Incorrect  😞")

print(f"Your score so far is {score} / 5.")

answer = input("""
4. What does USB stand for? """)
if answer.lower() == "universal serial bus":
    print("Correct!  😄")
    score += 1
else:
    print("Incorrect  😞")

print(f"Your score so far is {score} / 5.")

possible_answers = ["matt", "matthew", "matt keeble", "matthew keeble"]
answer = input("""
5. Who is the best husband in the world? """)
if answer.lower() in possible_answers:
    print("Correct!  😄")
    score += 1
else:
    print("Incorrect  😞")

print(f"Your final score is {score} / 5.")
print("""
Thank you for playing!!
      """)
input("Press enter to quit.")