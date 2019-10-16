import random

#generates random number
randomnumber = random.randint(1,10)

#prompts user for input number
guess = input('Guess a number between 1 and 10'   )
guess = int(guess)

#tests if guess is correct, if not, asks for another guess
if guess == randomnumber:
    print('Yes, you are correct!')
else:
    guess = int(input('Nope! Guess a different number between 1 and 10'))
    #tests if the second guess is correct, if not, asks for another guess
    if guess == randomnumber:
        print('Yes, you are correct!')
    else:
        guess = int(input('Nope !Guess a different number between 1 and 10'))
        #tests if your third guess is correct, if not, informs you that you have lost the game
        if guess == randomnumber:
            print('Yes, you are correct!')
        else:
            print('Nope, you loose!')
            
