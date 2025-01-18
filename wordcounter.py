 #find the number of words in a sectence
#example : hello world has 2 words with saperated by space

#use : 
#1. user input
#2. functions
#3. f-string

#count only word

def count_word(sentence):
  word_list=sentence.split()
  
  return len(word_list)
user_input=input("Enter a sntance or paragraph to count the word : ")

count=count_word(user_input)
print(f"number of word in your sentence is : {count}")