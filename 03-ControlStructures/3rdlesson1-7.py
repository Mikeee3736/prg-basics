###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.30 # 30%
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'

if is_bonus:
    total_salary = basic_salary+0.3*basic_salary
    print(f' Your salary witrh 30% bonus included is: {total_salary}')
else:
    print(f'Your salary is: {basic_salary}')
