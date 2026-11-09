# Write a program that calculates values for the following fractions: 1/2, 1/3, ..., 1/10. Sample result:

# 1/1 = 1.0
# 1/2 = 0.5
# 1/3 = 0.3333333333333333
# ...
# 1/10 = 0.1

###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#
division=0 
for i in range(0,10):
    division= 1/(i+1)
    print(f'1/{i+1} = {division}')