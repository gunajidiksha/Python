import math

angle_degrees = float(input("Enter the angle in degrees : "))
length_x = float(input("Enter the length of x : "))
length_y = float(input("Enter the length of y : "))

angle_radians = math.radians(angle_degrees)

z = (length_x*math.cos(angle_radians))+(length_y*math.sin(angle_radians))

print("The result = ",z)