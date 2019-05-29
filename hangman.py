import sys
import random

def hangman_pattern(guess):
    if (guess == 0):
        print("_________")
        print ("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif (guess == 1):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif (guess == 2):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	 |")
        print("|	 |")
        print("|")
        print("|________")
    elif (guess == 3):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|")
        print("|	 |")
        print("|")
        print("|________")
    elif (guess == 4):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|")
        print("|________")
    elif (guess == 5):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ ")
        print("|________")
    elif (guess == 6):
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ \ ")
        print("|________")
        print("\n")


def game():
    print("Lets play Hangman")
    lines = open('hangman.txt').read().splitlines()
    word = random.choice(lines)
    print(word)
    length_word = len(word)
    guess = 0
    hangman_pattern(guess)
    i = 1
    dash = []
    all_guesses = []
    while i<=length_word:
        dash.append('-')
        i=i+1
    print(' '.join(dash))
    print("\n")
    while guess<=6:
        letter = input("Guess a letter ")
        i = 0
        w = list(word)
        if len(letter) > 1:
            print("You can enter single letter at a time")
        elif len(letter) == 0:
            print ("Don't leave it blank")
        elif letter in all_guesses:
            print ("You have already entered the letter")
        else:
            all_guesses.append(letter)
            while i<length_word:
                if letter in word[i]:
                    n = i
                    dash[n] = letter
                i= i + 1
            print(' '.join(dash))
            if dash == w:
                print("You guessed right")
                choice = int(input("Would you like to play again,type 1 for yes or 2 for no"))
                if choice == 1:
                    game()
                elif choice == 2:
                    sys.exit()
            if letter not in word:
                guess = guess + 1
                hangman_pattern(guess)

            print("\n")
        if guess == 6:
            print("The word was",word)
            print("You loose")
            choice = int(input("Would you like to play again,type 1 for yes or 2 for no"))
            if choice == 1:
                game()
            elif choice == 2:
                sys.exit()
game()

