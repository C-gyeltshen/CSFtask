user_number = int(input("enter a number :"))
factural = 1

for i in range(1, user_number + 1):
    factural *= i

print(f"factorial of {user_number} is {factural}")

