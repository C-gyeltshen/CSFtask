num1 = int(input("Enter a Number1 :"))
num2 = int(input("Enter a Number2 :"))

second = 0
first = 0
if num1 > num2:
    second = num1
    first = num2
else:
    second = num2
    first = num1

print (second)
print (first)

num = []
while first != second:
    first += 1
    if first == second:
        break
    else:
        num.append(first)
print("sum :",sum(num))

# result = 0
# while first != second:
#     result = result + first
#     first = first + 1

# print(result)