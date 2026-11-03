###
# Credit card payment 
#
account_balance = 500
total_payment = input("Enter your total payment: ")
total_payment= int(total_payment)
if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')