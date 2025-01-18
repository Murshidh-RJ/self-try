user_input = int(input("Please enter a number to check if its a prim eor not : "))

def is_prime (number):
  if number <2:
    return False 
  for i in range (2,number):
    if number % i == 0:
      return False
  
  return True

validation = is_prime(user_input)

if validation:
  print(f"{user_input} is a prime number ")
else:
  print(f"{user_input} is not a prime number")