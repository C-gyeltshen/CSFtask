guess = False
while guess != True:
    import random
    secret_number = random.randint(1,4)
    
    user_guess = int(input("Guess a number between 1 to 100 :"))

    if user_guess == secret_number:
        guess = True

print (f"Oh yeah your guess number {secret_number} and secret number generated {secret_number} is same ")




