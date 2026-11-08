# Write a program that calculates and prints the quarter of the year for a given month number (1..12). Then check the program's results for the months:

# 12, 10, 9, 1

# ###
# # Calculates and prints the quarter of the year for a given
# # month number (1..12)
# #
month= int(input("Enter month number from 1 to 12:  "))
if month>= 10:
    print(f"The month {month} is in the fourth quarter")
elif 7<= month <10:
    print(f"The month {month} is in the third quarter")
elif 4<= month <7:
    print(f"The month {month} is in the second quarter")
elif 1<= month<4 :
    print(f"The month {month} is in the first quarter")
