"""
Codecademy - Learn Python
Area Calculator
This program will ask the user to choose a shape,
then it will return the area of that shape
"""

print('Area calculator is starting')

# ask user to select a shape and store input to variable
option = input("Enter C for Circle or T for Triangle: ")

# check if user has selected 'C' or 'T'
if option == 'C':
    # convert input string into floating point number with float()
    radius = float(input("Enter radius: "))
    pi = 3.14159
    # calculate area of circle
    area = pi * radius**2
    # print area using string formatting
    print("Area: %f" % area)
elif option == 'T':
    # get base and height from user
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    # calculate area of triangle
    area = 0.5 * base * height
    print("Area: %f" % area)
else:
    print("Invalid Shape")

print("Exiting Program. Goodbye...")
