###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1= int(input("Enter first number: "))
number2= int(input("Enter second number: "))
operator= input("Enter operator (+, -, *, /) : ")

if operator =="+":
    sum= number1+number2
    print(f"The result is: {sum}")

elif operator== "-":
    substraction= number1- number2
    print(f"The result is: {substraction}")

elif operator == "*":
    multiplication = number1*number2
    print(f"The result is: {multiplication}")

elif operator == "/":
    division = number1/number2
    print(f"The result is: {division}")

else:
    print("Invalid data")