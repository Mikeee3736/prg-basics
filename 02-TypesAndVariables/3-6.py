import math
height=input("height of the observer above the ground in meters:")
height= int(height)

distance_to_the_horizon=3.57*(math.sqrt(height))
print("Distance to the horizon in kmis:", distance_to_the_horizon)

