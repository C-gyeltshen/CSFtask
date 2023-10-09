user_name = input("enter a name :").lower()

num_vowels = 0
vowels = "aeiou"
for i in user_name:
    if i in vowels:
        num_vowels += 1

print(num_vowels)