username = input("enter a name :").lower()
vowels = 0
index = 0

while index < len(username):
    if "a" == username[index]:
        vowels += 1
    elif "e" == username[index]:
        vowels += 1
    elif "i" == username[index]:
        vowels += 1
    elif "o" == username[index]:
        vowels += 1
    elif "u" == username[index]:
        vowels += 1

    index += 1 

print(vowels)
       
   

