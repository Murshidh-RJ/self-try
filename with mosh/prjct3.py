#rock paper scissor game
#ask the user to choice
#if choise is not valid 
# print error
#let the computer make a choise
#print both choices
#determine the winner
#ask the user if want to contniue
#if not terminate 
import random
choice_tuple=('r','p','s')
while True:
  user_choice=input("make you choise Rock ,Paper or Scissors? (r/p/s): ").lower()
  if user_choice not in choice_tuple:
    print("please enter a valid input")
    continue
  else:
    com_choice=random.choice(choice_tuple)
    print(f"You chose {user_choice} and computer chose {com_choice}")
    if com_choice==user_choice:
      print("its a draw!!")
    elif ((com_choice=='p'and user_choice=='s') or
         (com_choice=='s' and user_choice=='r') or
         (com_choice=='p' and user_choice=='r')):
      print(f"user wins!!")
    else:
      print("You lose")
    decision=input("Do you want to contnue ? ").lower()
    if decision=='y':
      continue
    else:
      break