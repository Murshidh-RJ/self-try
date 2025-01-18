#input - 12345
#output 1+2+3+4+5

#use : 
#1 - list coprehension
#2 - f-string

#additional task : 
#1. Take input from users
user_input = input("Enter the number you want to add each number from that : ")
sum_nums = sum(int(i)for i in user_input)


print(f"total of the numbers of elemnt {sum_nums}")