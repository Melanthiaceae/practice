#!/usr/bin/env python
# -*- coding: utf-8 -*-

#This is a Hangman Game!
#Imports
import random

#Get the word list from the text file, and make it a python list
wordfile = open("wordlist.txt", "r")    
words = wordfile.read()    
wordfile.close()
wordlist = words.split()
#Uncomment the next line to print this wordlist for debugging
#print(wordlist)    

#Set some global variables for stat tracking
games_won = 0
games_lost = 0

#Function to choose a random word from the list. Make it lowercase to avoid case issues    
def new_word():
    word = random.choice(wordlist)
    return word.lower()

#Introduce the game...      
print("Lets play Hangman!")
print

#List to get the right hangman picture!
the_man = [" --------------- \n¦    _______    ¦\n¦   |      |    ¦\n¦   |      |    ¦\n¦   |      O    ¦\n¦   |    --I--  ¦\n¦   |     / \   ¦\n¦  _|________   ¦\n¦               ¦\n --------------- \n"," --------------- \n¦    _______    ¦\n¦   |      |    ¦\n¦   |      |    ¦\n¦   |      O    ¦\n¦   |    --I--  ¦\n¦   |           ¦\n¦  _|________   ¦\n¦               ¦\n --------------- \n"," --------------- \n¦    _______    ¦\n¦   |      |    ¦\n¦   |      |    ¦\n¦   |      O    ¦\n¦   |      I    ¦\n¦   |           ¦\n¦  _|________   ¦\n¦               ¦\n --------------- \n"," --------------- \n¦    _______    ¦\n¦   |      |    ¦\n¦   |      |    ¦\n¦   |      O    ¦\n¦   |           ¦\n¦   |           ¦\n¦  _|________   ¦\n¦               ¦\n --------------- \n"," --------------- \n¦    _______    ¦\n¦   |      |    ¦\n¦   |      |    ¦\n¦   |           ¦\n¦   |           ¦\n¦   |           ¦\n¦  _|________   ¦\n¦               ¦\n --------------- \n"," --------------- \n¦    _______    ¦\n¦   |           ¦\n¦   |           ¦\n¦   |           ¦\n¦   |           ¦\n¦   |           ¦\n¦  _|________   ¦\n¦               ¦\n --------------- \n"," --------------- \n¦               ¦\n¦   |           ¦\n¦   |           ¦\n¦   |           ¦\n¦   |           ¦\n¦   |           ¦\n¦  _|________   ¦\n¦               ¦\n --------------- \n"," --------------- \n¦               ¦\n¦               ¦\n¦               ¦\n¦               ¦\n¦               ¦\n¦               ¦\n¦  __________   ¦\n¦               ¦\n --------------- \n"," --------------- \n¦               ¦\n¦               ¦\n¦               ¦\n¦               ¦\n¦               ¦\n¦               ¦\n¦               ¦\n¦               ¦\n --------------- \n"]

#Function that runs the main game.
def gametime():
    #Calls the function to pick a word
    word_str = new_word()
    #Sets the lives
    lives = 8
    
    #Primes a blank list to store guessed letters so you don't double guess.
    lets_guessed = []
    
    #Uncomment the next line to print the target word for debugging
    #print("Debug: Word is " + word_str)

    #Prime the guessed characters list as underscores - length matches the target word
    guess_lst = ["_"] * len(word_str)
    
    #Tell the player the word length, and print the guessed list (which is just underscores at this point)
    print("Your word is " + str(len(word_str)) + " letters long.")
    print
    print(" ".join(guess_lst))
    print
    print("You have " + str(lives) + " lives remaining")
    print the_man[lives]

    #Loop whilst we still have some lives
    while lives > 0:
        #Prompt for the guess letter
        print("Your guesses so far are: " + " ".join(lets_guessed))
        print("So far, you've got: " + " ".join(guess_lst))
        guess_raw = raw_input("Guess a single letter! ")
        #Make it lowercase to avoid case issues
        guess = guess_raw.lower()
        #Backdoor to force the program to stop, mostly for debugging
        if guess == "exit":
            lives = 0
            print ("Exiting")
        #If the player has entered more than one character, reject the guess
        elif len(guess) != 1:
            print( guess + " is not a single letter. Try again.")
        #If the player has entered a non-alphabetic character, reject the guess
        elif guess.isalpha() == False:
            print( guess + "is not a letter! Try again!")
        #now we know it's a single, alpha character, test the guess
        else:
            #Set already guessed to false so we can change it in the below check
            already_guessed = False
            #Check if the letter has already been guessed
            for l in lets_guessed:
                if guess == l:
                    already_guessed = True
            #Set the postion of the letter, and the number of correct guesses, to 0 for the coming iteration
            let_pos = 0
            let_count  = 0
            #Iterate through each character in the target word, and compare it to the guess
            for char in word_str:
                    #If the guess matches the character
                    if guess == char:
                        #Replace the underscore in the guess list with the relevent letter
                        guess_lst[let_pos] = guess 
                        #Set the number of correct guesses for this guess to +1
                        let_count += 1
                    # Set the letter postion for this gues to +1 before running through the loop again
                    let_pos += 1
            #If 1 (or more) letters have been found, Congratulations and show the updated guessed list
            if already_guessed:
                    print
                    print("You have already guessed " + guess + ". Try a different letter")
                    print
            elif let_count > 0:
                #Add the letter to the letters guessed
                lets_guessed.append(guess)
                #Congratulate the player, and print the letters in the guess word
                print
                print("Congratulations! You found a letter!")
                print(" ".join(guess_lst))
                print
                #If the guessed list is now the same as the word, you win!
                if "".join(guess_lst) == word_str:
                    global games_won
                    games_won += 1
                    print
                    print("Congratulations! You win!")
                    print
                    #Prompt the player to play again
                    anothergo()
            #If no letters have been found in this go...
            else:    
                #Add the letter to the letters guessed
                lets_guessed.append(guess)
                #Reduce lives by 1
                lives -= 1
                # Tell the player we've reduced their lives remaining
                print
                print("Sorry, " + guess + " is not in the target word. You have " + str(lives) + " lives remaning!")
                print
                print the_man[lives]
                print
                #If the player is out of lives, end the game.
                if lives == 0:
                    global games_lost
                    games_lost += 1
                    print
                    print("Game over! The word was " + word_str + ".")
                    print
                    #Prompt the player to play again
                    anothergo()
                # If the player still has lives, the loop will run again.

#Function to prompt the player for another game               
def anothergo():
    #Set the lives to 0, otherwise when the script ends it will return the player into the last game if they won
    lives = 0
    #Work out the current percentage, and feed that, plus the number won/lost into a stats string, then print it.
    games_dec = float(games_won) / (float(games_won) + float(games_lost))
    games_pct = "{:.1%}".format(games_dec)
    stats = "You have won " + str(games_won) + " games and lost " + str(games_lost) + " games. That's a win rate of " + games_pct + "."
    print(stats)
    print
    #Ask for a Y/N response
    play_again = raw_input("Would you like to play again? Enter Y/N")
    #Make that response lowercase, to avoid case issues
    play_again_low = play_again.lower()
    #If they enter something else, ask again
    if play_again_low != "y" and play_again != "n":
        print("You did not enter 'Y' or 'N'")
        anothergo()
    #If they say yes, run the main game function again (note this generates a new word)
    elif play_again_low == "y":
        gametime()
    #If they want to leave, say good bye
    else:
        print("Okay! See you later!")
        exit()
        #The script will exit here.

#This starts the first game, after everything else has been declared.
gametime()
