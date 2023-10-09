username = input("enter a name :").lower()

result = False 
index = 0
while index < len(username):
    if "a"==username[index]:
        result = True 
    elif "e"==username[index]:
        result = True
    elif "i"==username[index]:
        result = True
    elif "o"==username[index]:
        result = True
    elif "u"==username[index]:
        result = True 
    index += 1

print(result)
    
