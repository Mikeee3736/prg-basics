# The parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:

# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN
# Write a program that asks for the number of hours of parking, then calculates and prints the correct fee.


parking_hours = int(input("Enter the number of hours parking: "))
if 1<= parking_hours <= 2 :
    print("pay 5 pln")

elif 3<= parking_hours <=6 :
    print("pay 15 pln")

elif parking_hours >6:
    print("pay 20 pln")
