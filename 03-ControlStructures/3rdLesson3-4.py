###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
first_number= int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
if first_number>=0 or second_number>=0 :
    print("at least one number entered from the keyboard is not negative")
else: 
    print("both numbers are negative")
