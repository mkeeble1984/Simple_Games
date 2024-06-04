import time
import os
import sys

repeat = "Y"

while repeat == "Y":
    while True:
        story = ""
        words = set()
        start_or_word = -1
        os.system("cls")

        print("Noun = Naming word (John, house, teacher, river)")
        print("Verb = Doing word (sleep, jumping, eat, thinking)")
        print("Adjective = Describing word (beautiful, tall, fast, tired)")
        print("Adverb = Describes a doing word (softly, strangely, loudly, very)")
        which_story = input("\nSelect a story (a, b or c): ").lower()
        print("")
        if which_story == "a":
            with open("C:\\Users\mkeeb\OneDrive\Documents\Matt\Programming\Simple Games\Madlibs_Stories\story_a.txt", "r") as f:
                story = f.read()
                break;

        elif which_story == "b":
            with open("C:\\Users\mkeeb\OneDrive\Documents\Matt\Programming\Simple Games\Madlibs_Stories\story_b.txt", "r") as f:
                story = f.read()
                break;

        elif which_story == "c":
            with open("C:\\Users\mkeeb\OneDrive\Documents\Matt\Programming\Simple Games\Madlibs_Stories\story_c.txt", "r") as f:
                story = f.read()
                break;

        else:
            print("\nPlease eneter a valid choice. (a, b or c)")
            time.sleep(3)
            os.system("cls")

    for i, char in enumerate(story):
        if char == "<":
            start_or_word = i
        
        if char == ">" and start_or_word != -1:
            word = story[start_or_word: i + 1]
            words.add(word)
            start_or_word = -1
    
    answers = {}

    for word in words:
        answer = input(f"Enter a word for {word}: ")
        answers[word] = answer

    for word in words:
        story = story.replace(word, answers[word])

    print("")
    print(story)
    print("")

    while repeat != "Y" or repeat != "N":
        repeat = input("Would you like to play again? (Y / N): ").upper()
        if repeat == "Y":
            break
        elif repeat == "N":
            break
        # sys.exit(0)
        else:
            print("\nPlease eneter a valid choice. (Y / N)")
            time.sleep(4)
            os.system("cls")

