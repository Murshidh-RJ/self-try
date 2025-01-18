#converting given celcius to ferenhite

user_input=int(input("Please enter the celcius amount you want to convert to frenhite : "))

Ferenhite = (user_input*9/5) + 32
print(f"{user_input} degre celsius is {Ferenhite} degree frenhite")




def celcius_To_ferenhite(c):
  ferenhite = (c*9/5) +32
  return ferenhite

user_in = int(input("Enter the number to convert : "))
converted=celcius_To_ferenhite(user_in)
print(f"converted is {converted}")