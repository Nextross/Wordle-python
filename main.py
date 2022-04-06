from random import choice
from sys import exit
from words import english_wordle_list, english_words_valid


#  Checks if user_word is in English word list
def word_validation(word_list, word):
    start = 0
    end = len(word_list) - 1

    while start <= end:
        middle = (start + end) // 2

        if word_list[middle] > word:
            end = middle - 1
        elif word_list[middle] < word:
            start = middle + 1
        else:
            return True

    return False


#  Returns random word depending on player's choice of game language
def choose_word(option):
    options = "1"  # For multiple languages later

    while option not in options:
        print("\nWrong input, try again")
        option = input("Please select number:\n\n1 - English\n2 - Czech\n\nYour option: ")

    if option == "1":
        print("You chose English as your game language\n")
        return choice(english_wordle_list)


#  Returns indications of correct/incorrent letter placements
def letter_placement(user_word_list):
    signs = "[ "

    for index, letter in enumerate(user_word_list):
        if letter == chosen_word[index]:
            signs += "O "
        elif letter in chosen_word:
            signs += "? "
        else:
            signs += "X "

    return signs + "]"


chosen_word = choose_word(input("Please select number:\n1 - English\n\nYour option: "))
print("Type a word")

attempts = 0  # Doesn't include wrong inputs
user_word = ""  # This is what the user will put as input

while user_word != chosen_word:
    user_word = input("> ").strip().lower()
    if user_word.strip().lower() == "giveup":
        print(f"You gave up (total attempts: {attempts}), the correct answer was: {chosen_word.upper()}")
        exit()

    attempts += 1

    #  Checks if user_word is valid - 5 chars. long, only letters, is in English words list
    while len(user_word) != 5 or not user_word.isalpha() or not word_validation(english_words_valid, user_word):
        print("Wrong input, try again")
        user_word = input("> ").strip().lower()

    print(f"[ {user_word[0].upper()} {user_word[1].upper()} {user_word[2].upper()} {user_word[3].upper()} {user_word[4].upper()} ]")
    print(letter_placement(list(user_word)))

print(f"\nYOU WON, the correct answer was {chosen_word.upper()}\nTotal attempts: {attempts}")
