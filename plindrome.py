user_input=input("ENter a string to check if its a palindrome or not : ")


def is_palindrome(word):
  word=word.lower()
  new_word=word[::-1]
  if new_word == word:
    return True
  return False

if is_palindrome(user_input):
  print(f"{user_input} is a palindrome")
else:
  print(f"{user_input} is not palindrome")
 