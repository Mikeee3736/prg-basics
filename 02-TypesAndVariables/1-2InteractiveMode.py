PS C:\Users\dmytr\ComputerProgramming\prg-basics> python                                  
Python 3.15.2 (tags/v3.15.2:5e58eaa, Oct 25 2026, 17:27:03) [MSC v.1951 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Ctrl click to launch VS Code Native REPL (https://aka.ms/python-native-repl)
>>> 7+4
11
>>> (30+10)/2
20.0
>>> 2**3
8
>>> 7>5
True
>>> r=4
>>> area = 3.14159 * r * r
>>> area
50.26544
>>> round(area,2)
50.27
>>> first_name="Mary"
>>> last_name="Brown"
>>> full_name= first_name +''+ last name
  File "<python-input-10>", line 1
    full_name= first_name +''+ last name
                                    ^^^^
SyntaxError: invalid syntax
>>> full_name= first_name +''+ last_name
>>> full_name
'MaryBrown'
>>> full_name= first_name +"  "+ last_name
>>> full_name
'Mary  Brown'
>>> print(full_name)
Mary  Brown
>>> len(full_name)
11
>>> a=5
>>> h=4
>>> area_triangle= 0.5*5*4
>>> area_triangle
10.0
>>> arithmetic_mean=(7+12+31)/3
>>> round(arithmetic_mean,2)
16.67
>>> 