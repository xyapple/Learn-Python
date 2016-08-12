# This is a random guess game
import random
print('I am thinking of a number between 1 and 20. \n Please enter an number')

guessNu = random.randint(1,21)
guess = int(input())

for n in range (1,6):
    print('Please enter a number')
    userGuess = int(input())

    if userGuess < guessNu:
        print('your number is too low. \n Please try again')
    elif userGuess > guessNu:
        print('your number is too high. \n Please try again')

    else:

        break

if userGuess == guessNu:
    print('You are right!! Yeah!!')
else:
    print('The correct number is '+ str(guessNu) +' Thank you for playing!')


