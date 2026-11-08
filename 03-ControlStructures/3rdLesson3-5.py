# Write a program that calculates and prints the number of days in a given month (1..12). Assume that February always has 28 days.

# ###
# # Calculates the number of days in a month
# #
month= int(input( "Enter month number: "))
if month ==1 or month== 3 or month ==5 or month== 7 or month== 8 or month==10 or month==12 :
    print(f"Number of days in month {month} is 31")

elif month ==2 :
    print(f"Number of days in month {month} is 28")

else:
    print(f"Number of days in month {month} is 30")