price= input("Enter price:")
price= float(price)
price= round( price,2)
discount = input("Enter discount %:")
discount= int(discount)
reduction= price*(discount/100)
price_with_discount= price-reduction
reduction= round( reduction,2)
price_with_discount= round(price_with_discount,2)
print(f"Price with discount: {price_with_discount}")
print(f'Reduction: {reduction}')


