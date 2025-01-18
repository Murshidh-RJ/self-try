a =12
b = 36

def calc_gcd(num1,num2):
  while(num2):
    print("starting")
    print(num1)
    print(num2)
    num1 ,num2 = num2, num1%num2
    print("After %")
    print(num1)
    print(num2)

  return num1

gcd = calc_gcd(a,b)
print(f"GCD of {a} and {b} is {gcd} ")
