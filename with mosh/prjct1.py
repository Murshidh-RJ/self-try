import random
#loop
  #ask : roll the dice ?
while True:
  response=input("Do you want to roll the dice(y/n) ? ").lower()
  #if user enters y
  if response == 'y':
  # generate 2 random numbers
    random_num1=random.randint(1,6)
    random_num2=random.randint(1,6)
  # print them
    print(f"{random_num1,random_num2}")
  #if the user enters n
  elif response =='n':
  #  say thank you message

    print("Thank you for playing the game ")
  # terminate
    break
  #else
  else:
    print("Invalid choise ")
  # print invalid choice