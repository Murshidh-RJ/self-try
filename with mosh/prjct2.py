#number guessing game
#ask the user to geuss a number from 1 to 100
#ask the computer to guess a number 
#if not a valid number 
# print error
#if number< guess
#  too low
#if number > guess
#   too high
#else 
# well done

import random
com_guess=random.randint(1,100)

while True:
  try:
    user_guess=int(input("Enter a number fro 1 to 100 : "))
    if user_guess<1 or user_guess>100:
      continue
    if user_guess<com_guess:
      print('Too low')
    elif user_guess>com_guess:
      print("Too high ")
    else:
      print("congratulations you guessed it correct ")
      break
  except ValueError:
    print("Please enter a valid number")
    continue

