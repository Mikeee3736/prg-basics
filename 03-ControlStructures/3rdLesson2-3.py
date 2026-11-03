# The car has three driving modes: Auto (A), Manual (M) and Eco (E). In each of these three modes, the average fuel consumption in liters per 100 km is 7, 9 and 6 respectively. Write a program that calculates total fuel consumption for a given distance in km and a given driving mode. Then, calculate the total fuel consumption for the following data:

# distance 200 km, driving mode M (the result should be 18 liters)
# distance 400 km, driving mode A (the result should be 28 liters)
# distance 350 km, driving mode E (the result should be 21 liters)
# ###
# # The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#
driving_mode= input("Please enter your driving mode Auto (A), Manual (M) or Eco (E): ")
distance=  int(input("Enter the distance in km: "))
if driving_mode== "A":
    total_fuel_consumption= (distance/100)*7
    print(f"Your total fuel consumptiopn is: {total_fuel_consumption}")

elif driving_mode== "M":
    total_fuel_consumption= (distance/100)*9
    print(f"Your total fuel consumptiopn is: {total_fuel_consumption}")

elif driving_mode== "E":
    total_fuel_consumption= (distance/100)*6
    print(f"Your total fuel consumptiopn is: {total_fuel_consumption}")

else:
    print("Invalid data. Please enter A,M or E")