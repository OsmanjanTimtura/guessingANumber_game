#User guesses an integer between 0-9 for 3 times, user wins if guessed correctly, or user fails after trying to guess 3 times unsuccessful. 

from random import randint
user_wants_to_play = True

#This function takes a number from the user, if user input is an integer it proceeds. Else, it requests user to enter again. 
def guessAnumber(myGuess):
    #confirm user guessed an integer.
    guessAnumber = False
    while guessAnumber is False:
        try:
            myGuess = int(myGuess)
            guessAnumber = True
        except:
            myGuess = input("Not an integer! Try again!\nPlease enter an integer in range 0-9! ") 

    return myGuess


#This function confirms user input is an integer in range, else it requests user to enter again. 
def guessAnInRangenumber(myNumber):
    #confirm user guessed an integer in range.
    guessAnInRangenumber = False
    while guessAnInRangenumber is False:
        if 0 <= myNumber <= 9:
            guessAnInRangenumber = True
        else:
            myNumber = input("This integer is not in range! Try again!\nEnter an integer between 0-9!")
            myNumber = guessAnumber(myNumber)
    
    return myNumber


#While loop makes sure user has a choice to play again at the end. 
while user_wants_to_play:
    #This counts user guesses.
    guessCount = 0
    #This randomly selects an integer between 0-9.
    secretNumber = randint(0,10)
    #User guesses 3 times before successully guessing the secret number, or fails. 
    while guessCount in range(3):
        #requesting user to guess a number
        userGuess = input("Enter an integer in range 0-9: ")
        #This makes sure user guessed an integer. 
        userGuess = guessAnumber(userGuess)
        #This makes sure user guessed an integer in range of 0-9.
        userGuess = guessAnInRangenumber(userGuess)
        #Following conditional statements tell if user guessed correct or not. 
        #Before 3rd try, user is asked to guess higher if current guess a smaller integer than secret integer. 
        if userGuess < secretNumber:
            if guessCount != 2:
                print("Wrong! Guess higher!")
            else:
                print("Wrong again!")
            #Guess count increases by one.
            guessCount = guessCount + 1
        #Before 3rd try, user is asked to guess lower if current guess is a larger integer than secret integer. 
        elif userGuess > secretNumber:
            if guessCount != 2:
                print("Wrong! Guess lower!")
            else:
                print("Wrong again!")
            #Guess count increases by one.
            guessCount = guessCount + 1
        #User wins if guessed correctly. And game ends right away. 
        else:
            print("Great! You won!")
            break
    #User falis once guessed wrong 3 times. 
    else:
        print("You already guessed 3 times, you lost!")
    #User asked if wanted to play again. 
    user_has_intention = input("\nDo you want to play again?\nPress 'Y' to play again,\nPress any other key to exit\n")
    if user_has_intention.upper() != "Y":
        user_wants_to_play = False

