#taske list
#filter evens from list
#print new list

numbers=[1,2,3,4,5,6,7,8,9,23,54,56,12,32,44,54,234,657]

filred_list=[num for num in numbers if num % 2 == 0]

print(filred_list)