# Define a function time_string(hours, minutes, time_format) that, given the number of hours (0..23) and the number of minutes (0..59), returns a string specifying the time in the given format ('24' for 24-hour time and '12' for 12-hour time).

# Then write a program that tests whether the function works correctly.

# time_string(15, 38, '24') returns '15:38'
# time_string(8, 3, '24') returns '08:03'
# time_string(0, 5 '24') returns '00:05'
# time_string(11, 15, '12') returns '11:15am'
# time_string(0, 7, '12') returns '12:07am'
# time_string(7, 30, '12') returns '7:30am'
# time_string(12, 46, '12') returns '12:46pm'
# time_string(13, 10, '12') returns '1:10pm'
# time_string(19, 02, '12') returns '7:02pm'
# Hint: Use f-strings formatting. Search the Internet for 'Format numbers using f-strings
hours= int(input("Enter number of hours: "))
minutes= int(input("Enter number of minutes: "))
time_format=(input("Enter time format 12/24: "))
def time_string(hours, minutes, time_format):
    if time_format=='24':
        if hours>9 and minutes>9:
            result=f"{hours}:{minutes}"
        elif hours>9 and minutes<10:
            result=f"{hours}:0{minutes}"
        elif hours<10 and minutes<10:
            result=f"0{hours}:0{minutes}"
        elif hours<10 and minutes>9:
            result=f"0{hours}:{minutes}"
        
    elif time_format== '12':
        if hours<12:
            if hours>9 and minutes>9:
                result=f"{hours}:{minutes}am"
            else:
                result=f"{hours}:0{minutes}am"
        if hours==12:
             if hours>9 and minutes>9:
                result=f"{hours}:{minutes}pm"
             else:
                 result= f"{hours}:0{minutes}pm"
            
            
        if hours>12: 
             if hours>9 and minutes>9:
                result=f"{hours-12}:{minutes}pm"
             else:
                result=f"{hours-12}:0{minutes}pm"
    return result
print(time_string(hours, minutes, time_format))

