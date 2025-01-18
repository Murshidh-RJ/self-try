#calculate the lcm 
import math

def calc_lcm(a,b):
  gcd = math.gcd(a,b)
  lcm = (a*b)//gcd
  return lcm

a=int(input("Enter a number to to calculate the lcm : "))
b=int(input("Enter a number to to calculate the lcm : "))

lcm = calc_lcm(a,b)
print(f"the lcm of {a},{b} is {lcm}")