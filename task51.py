num1 = int(input ("Enter a number :"))
num2 = int(input ("Enter a number :"))

second = 0
first = 0

if num1 > num2:
    second = num1
    first = num2 
else:
    second = num2 
    first = num1 

result = 0
for i in range(first + 1, second):
    result = result + i
   
print (result)