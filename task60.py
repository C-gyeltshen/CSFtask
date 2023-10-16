def is_even(num):
    div = num / 2
    if div != int(div):
        return True
    else:
        return False

print(is_even(5)) 
