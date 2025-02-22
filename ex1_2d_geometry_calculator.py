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

x1 = 1
y1 = 3
x2 = -2
y2 = -4

def calc_pythag_distance(x1, y1, x2, y2):
    if x1==x2 or y1==y2:
        raise ValueError("The triangle side lengths must be greater than 0.")
    else:
        pythag_distance = sqrt((x2-x1)**2 + (y2-y2)**2)
        return pythag_distance
    
def calc_angle(x1, y1, x2, y2):
    if x1==x2 or y1==y2:
        raise ValueError("The triangle side lengths must be greater than 0.")
    else:
        angle = degrees(atan((y2-y1)/(x2-x1)))
        return angle
    
pythag_distance = calc_pythag_distance(x1, y1, x2, y2)
print(pythag_distance)

angle = calc_angle(x1, y1, x2, y2)
print(angle)



