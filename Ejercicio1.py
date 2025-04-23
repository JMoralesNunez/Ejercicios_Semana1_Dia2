num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

highest = 0

if num1 > num2 and num1 > num3:
    highest = num1
    print(f"the biggest number is: {highest}")
elif num2 > num1 and num2 > num3:
    highest = num2
    print(f"the biggest number is: {highest}")
else:
    highest = num3
    print(f"the biggest number is: {highest}")