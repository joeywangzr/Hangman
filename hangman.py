import random
import re
from words import word_list

while True:
    chances = 10
    correctGuess = []
    incorrectGuess = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Select a random word
    random_word = word_list[random.randint(0,(len(word_list)-1))]
# Enable this if you want to see the answer
#    print(random_word)

    # Hide the word
    hidden_word = re.sub("[a-zA-Z]", "_", random_word)
    print("H A N G M A N")
    print("You have 10 chances to guess the hidden word!")
    print(hidden_word)

    #Loops through until all letters are correct
    while hidden_word != random_word:
        
    # Checks to see if user has a valid input
        user_letter = input("Pick a letter: ").lower()
        if len(user_letter) > 1:
            print("Please input 1 letter only!")
            print(hidden_word)
            print("You have " + str(chances) + " chances remaining")
        elif user_letter not in alphabet:
            print("Please input a letter!")
            print(hidden_word)
            print("You have " + str(chances) + " chances remaining")
        else:
# Compares against guessed letters
            if user_letter in (correctGuess or incorrectGuess):
                print("You have already guessed this letter. ")
                print(hidden_word)
                print("You have " + str(chances) + " chances remaining")
            elif user_letter not in random_word:
                print(user_letter + " is not in the hidden word. Try again.")
                print(hidden_word)
                incorrectGuess.append(user_letter)
                chances -= 1
                print("You have " + str(chances) + " chances remaining")
            else:
                print(user_letter + " is in the hidden word.")
                indexPos = 0
                while indexPos < len(random_word):
                    if random_word[indexPos] == user_letter:
                        index = random_word.find(user_letter, indexPos)
                        hidden_word = hidden_word[:index] + user_letter + hidden_word[index + 1:]
                    indexPos += 1
                    correctGuess.append(user_letter)
                print(hidden_word)
                print("You have " + str(chances) + " chances remaining")

        if chances <= 0:
            print("You lose.\nThe hidden word was: " + random_word)
            again = input("Play again? y/n ").lower()
            if again != ("n" or "y"):
                print("Please answer with y or n.")
        elif hidden_word == random_word:
            print("You got the hidden word right!")
            again = input("Play again? y/n ").lower()
            if again != ("n" or "y"):
                print("Please answer with y or n.")
        
    if again == "n":
        print("Thanks for playing.")
        break
    break