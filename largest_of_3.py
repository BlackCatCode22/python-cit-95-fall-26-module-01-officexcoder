num1 = int(input("Enter first interger: "))
num2 = int(input("Enter second interger: "))
num3 = int(input("Enter third interger: "))

# finding the largest number using nested if decisions
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3
print("The largest number is:", largest)