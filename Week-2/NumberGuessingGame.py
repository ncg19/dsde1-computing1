import random

#generates random number
randomnumber = random.randint(1,10)

#prompts user for input number
guess = input('Guess a number between 1 and 10'   )
guess = int(guess)

print(guess == randomnumber)
 