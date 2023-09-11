import random

word_length = 4
words = ["this", "four", "five", "help", "lake", "pink", "cats"]

hidden_word = random.choice(words)

def print_introduction():
    print("""\nWordle is a word guessing game.
    You have 5 attempts.
    (C) means the letter is in the word and in the correct position.
    (WP) means the letter is in the word but not in the correct position.
    (NT) means the letter is not in the word.
    Good Luck.""")

def check_word(guess):    
    if hidden_word == guess:
        print("Congrats! You are Winrar.")
        return 1
    else:
        result = ""
        for i,j in zip(guess, hidden_word):
            if i == j:
                result += "(C)"
            elif i in hidden_word:
                result += "(WP)"
            else:
                result += "(NW)"
        print(result)
        return 0

def main_loop():
    attempt = 5
    print_introduction()
    while attempt > 0:
        while 1:
            guess = input("Guess a four letter word: ")
            if len(guess) == word_length:
                break
            print("Not a four letter word, try again.")
        if check_word(guess):
            break
        else:
            attempt -= 1
            print(f"Attempts left: {attempt}")
    else:
        print("You Lose.")

main_loop()
