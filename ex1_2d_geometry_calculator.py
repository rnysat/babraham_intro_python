"""
Make a script which defines two 2D positions (x1, y1, x2, y2) and then calculates the distance between them (Pythagorean distance). 
Just make up some coordinates and put them in your script. 

• Also calculate the angle (in degrees) from the first point to the second 
• You will need to use the sqrt and atan functions from the math package for this, the angle will be in radians so you can use the degrees function from math to convert this.  
https://docs.python.org/3/library/math.html  
"""
from math import sqrt
from math import atan
from math import degrees
from math import pi
import random


def calc_pythag_distance(x1, y1, x2, y2):
    """Function to calculate the Pythagorean distance between two points supplied to the function via their x and y coordinates."""
    pythag_distance = sqrt((x2-x1)**2 + (y2-y1)**2)
    return pythag_distance
    
def calc_angle(x1, y1, x2, y2):
    """Function to calculate the angle, relative to a line parallel to the y=0 and passing through the x-coordinate
    of the first point, between two points supplied to the function via their x and y coordinates."""
    if (x2-x1) > 0 and (y2-y1) > 0:
        atan_output = atan((y2-y1)/(x2-x1))
        return degrees(atan_output)
    elif (x2-x1) < 0 and (y2-y1) > 0:
        atan_output = atan((y2-y1)/(x2-x1))
        quad_correction = pi - atan_output
        return degrees(quad_correction)
    elif (x2-x1) < 0 and (y2-y1) < 0:
        atan_output = atan((y2-y1)/(x2-x1))
        quad_correction = -(pi - atan_output)
        return degrees(quad_correction)
    elif (x2 > x2) > 0 and (y2-y1) <0:
        atan_output = atan((y2-y1)/(x2-x1))
        return degrees(atan_output)
    elif (x1 == x2) and (y2 - y1) >0:
        return 90
    elif (x1 == x2) and (y2 -y1) < 0:
        return -90
    elif (x2 - x1) > 0 and (y2 == y1):
        return 0
    elif (x2 - x1) < 0 and (y2 == y1):
        return 180
    elif (x2 == x1) and (y2 == y1):
        raise ValueError("Points must be non-identical in order to determine the angle between them relative to a line parallel to the x-axis (y = 0)")




x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))
    
pythag_distance = calc_pythag_distance(x1, y1, x2, y2)
print(pythag_distance)

angle = calc_angle(x1, y1, x2, y2)
print(angle)

help(random.uniform)







