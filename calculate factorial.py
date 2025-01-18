user_input=int(input("Please enter a number to get its factorial : "))
factorial = 1
number = 11
for i in range (1,12):
  factorial =factorial *i

print(factorial)

def count_fact(number):
  fact = 1
  for i in range (1,(number+1)):
    fact = fact *i

  return fact

results=count_fact(user_input)
print(f"Factorial of {user_input} is {results}")