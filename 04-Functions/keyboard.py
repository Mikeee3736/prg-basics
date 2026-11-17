# input_string() that returns a string entered from the keyboard
# input_integer() that returns an integer number entered from the keyboard
# input_real() that returns a real number entered from the keyboard
# input_boolean() that returns a boolean value depending on the pressed y/n key
def input_string(input1):
    input1= input("Enter your Name:")
    result= input1
    return result

def input_integer(input2):
    input2= int(input("Enter integer:"))
    result= input2
    return result

def input_real(input3):
    input3= float(input("Enter real number"))
    result= input3
    return result

def input_boolean(input4):
    input4= input("Ener y/n")
    result= input4
    return result== "y"