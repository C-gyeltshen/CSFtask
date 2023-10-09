user_name = input("enter a name :").lower()
result = 0
vowels = "aeiou"
for i in user_name:
    if i in vowels:
        result = True
    

print (result)