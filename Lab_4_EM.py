#---------------------------------
# Name:Essey Mehari
# Program: Lab_4_EM.py
#----------------------------------
#I certify that this work is mine
#----------------------------------
#Purpose: This program will play hangman with you
#----------------------------------
##imports the built-in random module which provides functions for generating random numbers.
 #creates a list called guess_list that contains a single element, a space.
 #imports the words list from a file called words.py. The words list  contains a collection of words that can be used in the program.
import random
guess_list = [" "]
from words import words

#This is a Python function called enter_guess() that takes a list of guessed_letters as an argument. The function does the following:
#Uses the input() function to prompt the user to enter a letter. The user's response is saved as the variable letter.
#Checks if the length of the letter variable is equal to 1 and if it is an alphabetic character using the len() and isalpha() functions, respectively.
#If the letter is already in the guessed_letters list, it prints a message telling the user they've already guessed that letter.
#If the letter is not in the guessed_letters list, the function returns the lowercase version of the letter using the lower() function.
#If the length of the letter is not equal to 1 or it is not an alphabetic character, the function prints a message saying that the input was invalid and to enter a single alphabetic character.
#The function returns the letter at the end
def enter_guess(guessed_letters):
    letter = input("Enter a letter: ")
    if len(letter) == 1 and letter.isalpha():
        if letter in guessed_letters:
            print("You already guessed this letter. Please try again.")
        else:
            return letter.lower()
    else:
        print("Invalid input. Please enter a single alphabetic character.")
    return letter
#gets a random word from the list of words found in words.py
def get_word(word_list):
    return random.choice(word_list)
#used to keep track of the number of incorrect guesses made by the user in the hangman game.
def hangman(target_word):
    incorrect_guesses = 0
    
    
def hangman(target_word):
    # Gallows parts
    #Defines the gallows parts of the hangman game (rope, head, right arm, torso, left arm, right leg, and left leg).
    rope = "\n--------\n" +' '*3+"|\n"
    head = "  O\n"
    right_arm = " /"
    torso = "|\n"
    left_arm = "\\"
    right_leg = "/\n"
    left_leg = "\\n"
    gallows_parts = [rope, head, right_arm, torso, left_arm, right_leg, left_leg]    
    # Initialize variables
    #letters_guessed: a list to keep track of the letters guessed by the player
    #incorrect_guesses: a count of the number of incorrect guesses made by the player
    #target_word_list: a list of the letters in the target word
    #display_word: a list of underscores representing the letters in the target word that have yet to be guessed    
    letters_guessed = []
    incorrect_guesses = 0
    target_word_list = list(target_word)
    display_word = ["_"] * len(target_word_list)

    # Game loop
    #Prints the current state of the word being guessed and the number of incorrect guesses
    #Calls the enter_guess() function to get a letter guess from the player
    #If the guess is in the target word, the corresponding letters in display_word are updated
    #If the guess is not in the target word, the number of incorrect guesses is incremented
    #The loop continues until either the target word has been fully guessed or the player has made 7 incorrect guesses    
    print("--------") # 8 dashes
    while "_" in display_word and incorrect_guesses < 7:
        print(" ".join(display_word))
        print("Incorrect Guesses: ",incorrect_guesses,end="")
        for i in range(incorrect_guesses):
            print(gallows_parts[i], end=" ")
        print("\n")
        print("letters guessed: ", end="")
        print(" ".join(sorted(letters_guessed)))

        guess = enter_guess(letters_guessed)
        letters_guessed.append(guess)
        if guess in target_word_list:
            for i in range(len(target_word_list)):
                if target_word_list[i] == guess:
                    display_word[i] = guess
        else:
            incorrect_guesses += 1

    # Display results
    #After the game loop, the final state of the word being guessed is displayed and the player is notified of their win or loss, along with the total number of guesses.
    print(" ".join(display_word))
    if "_" not in display_word:
        print("You took",len(letters_guessed),"guesses to guess '"+(target_word)+"'")
    else:
        print("Sorry, you took more than the allowed 7 incorrect guesses \nThe word was '"+target_word+"'")
    return None

def main():
    #Calls the get_word function, passing the words list as an argument. This function returns a random word from the words list.    
    #Calls the hangman function, passing the target_word as an argument. This function takes the target word as an input and runs the game logic to play Hangman.    
    target_word = get_word(words)
    hangman(target_word)
    return target_word


main()