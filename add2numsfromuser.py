#take 2 number from user and add together
#1. user input 
#2. function
#3. f-string

def add_nums(num1,num2):
  total=num1+num2

  return total

user_input1 = int(input("Enter a number to get sum : "))
user_input2 = int(input("Enter another number to get sum : "))

print(f"the total of {user_input1},{user_input2} is {add_nums(user_input1,user_input2)}")