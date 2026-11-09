# Write a program that asks the user for their age and then checks which age group they belong to:

# Child: under 13
# Teen: 13 to 19
# Adult: 20 to 64
# Senior: 65 or older

age= int(input("ENter your age:  "))

if age< 13:
    print("CHIld")

elif 13<= age <= 19 :
    print("teen")

elif 20 <=age <= 64:
    print("adult")

elif age> 65:
    print("Senior")
