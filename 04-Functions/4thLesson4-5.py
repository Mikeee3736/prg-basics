# Define a function that calculates the final grade for a test based on the number of points obtained, according to the rules:

# Less than 10 points, final grade: Fail
# At least 10 points, final grade: Satisfactory
# At least 14 points, final grade: Good
# At least 18 points, final grade: Excellent
points= int(input("Please enter the number of points: "))
def final_grade(points):
    if points< 10:
        result= "Fail"
        
    elif 14> points>=10 :
        result= "Satisfactory"
    elif 18> points>= 14:
        result= "Good"
    elif points>= 18:
        result= "Excellent"
    return result
    
print(f"Final grade: {final_grade(points)}")