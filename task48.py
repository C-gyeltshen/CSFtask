guess = False
import random
secret_number = random.randint(1,100)

while guess != True:
    
    user_guess = int(input("Guess a number between 1 to 100 :"))
    print (f" User guess is :{user_guess}")

    if user_guess == secret_number:
        print(f"Congratulations your guess is correct {secret_number}")
        guess = True
    elif user_guess > secret_number:
        print(f"Your guess is higher than secret number, guess a number less then {user_guess}")
    elif user_guess < secret_number:
        print(f"Your guess is less then the secret number, guess a number greater then {user_guess}")
    else:
        guess = False



    





