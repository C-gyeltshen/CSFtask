user_name = int(input("enter a number :"))

factorial = 1

current_number = 1 
while current_number <= user_name:
    factorial *= current_number
    current_number += 1
    
print (f"factorial of {user_name} is {factorial}")