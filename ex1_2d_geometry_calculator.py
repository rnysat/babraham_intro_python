"""
Make a script which defines two 2D positions (x1, y1, x2, y2) and then calculates the distance between them (Pythagorean distance). 
Just make up some coordinates and put them in your script. 

• Also calculate the angle (in degrees) from the first point to the second 
• You will need to use the sqrt and atan functions from the math package for this, the angle will be in radians so you can use the degrees function from math to convert this.  
https://docs.python.org/3/library/math.html  
"""
from math import sqrt
from math import atan
from math import sin
from math import cos
from math import degrees
from math import radians
from math import pi
import pytest
import random


def calc_pythag_distance(x1, y1, x2, y2):
    """Function to calculate the Pythagorean distance between two points supplied to the function via their x and y coordinates."""
    pythag_distance = sqrt((x2-x1)**2 + (y2-y1)**2)
    return pythag_distance
    
def calc_angle(x1, y1, x2, y2):
    """Function to calculate the angle between two points supplied to the function via their x and y coordinates.
    Point 1 has coordinates (x1, y1), and point 2 has coordinates (x2, y2).

     To maintain consistency between the output of the function and aid interpretation of the result, the angle is calculated relative to a line: 
     - parallel to y=0, 
     - passing through the x-coordinate of the first point, and 
     - with x coordinate greater than or equal to the x coordinate of the first point. 

     I will refer to a line that satisfies these criteria as the "positive x axis". 

     Diagram 1 depicts how this positive x axis is used to construct angles between two points. 
     Diagram 1 also labels the quadrants of the graph relative to this "positive x axis" as 1, 2, 3, and 4 moving anticlockwise.

     Data processing steps will be required in the function to account for the different positions that the second point could take in the grid depicted in diagram 1.
        The instructions for this exercise state that the atan function from the math package will need to be used.
        math.atan has an output range of (-pi/2, pi/2), exclusive, in radians, which is (-90, 90), exclusive, in degrees, for the input domain [-∞, ∞].

        In some instances, when the math.atan function is given an argument of (y2-y1)/(x2-x1), the output of the math.atan function matches the output that we require from the calc_angle() function. 
        This is the case when point 2 is in the first quadrant, including when it is positioned on the positive x axis.
        
        However, in other instances, the output of the math.atan function with argument of (y2-y1)/(x2-x1) must be modified in order to generate the output that we require from the calc_angle() function.
        When point 2 is in the second quadrant we require calc_angle() to return the value 135 degrees. In this scenario, the value of (y2-y1)/(x2-x1) might be -1.
        Whilst tan(135) = -1, 135 is not in the range [-90, 90]. Therefore, the solution returned is -45. Hence, the value needs to be adjusted by adding 180 (adding because quadrant 2 is a positive angle relative to the positive x axis, and 180 because this is the period of the tan graph).

        When point 2 is in the third quadrant, and the value of (y2-y1)/(x2-x1) is 1. The solution to atan(1) within the range (-90, 90) is 45 degrees. To achieve the correct output, we ned to subtract
        180 degrees (subtract because the value of the angle int he third quadrant relative to the positive x axis is negative, and 180 because this is the period of the tan graph).

        In still other instances, the math.atan function with argument of (y2-y1)/(x2-x1) will not generate an output because the value of (x2-x1) will be equal to zero and raise a ZeroDivisionError. 
        When point 2 is on the y axis, the value of (x2-x1) is zero, so cannot be a divisor in the input to atan. 

        These cases are accounted for using conditional statements."""
    #
    if ((x2-x1) > 0 and (y2-y1) >= 0) or ((x2 - x1) > 0 and (y2-y1) <0):
        atan_output = atan((y2-y1)/(x2-x1))
        return degrees(atan_output)
    elif (x2-x1) < 0 and (y2-y1) >= 0:
        atan_output = atan((y2-y1)/(x2-x1))
        quad_correction = pi + atan_output
        return degrees(quad_correction)
    elif (x2-x1) < 0 and (y2-y1) < 0:
        atan_output = atan((y2-y1)/(x2-x1))
        quad_correction = -pi + atan_output
        return degrees(quad_correction)
    elif (x1 == x2) and (y2 - y1) >0:
        return 90
    elif (x1 == x2) and (y2 -y1) < 0:
        return -90
    elif (x2 == x1) and (y2 == y1):
        raise ValueError("Points must be non-identical in order to determine the angle between them relative to a line parallel to the x-axis (y = 0)")


def test_calc_angle():

    #Test to confirm that the function runs
    calc_angle(0, 0, 1, 1)
    print("Function runs correctly.")

    #Test to confirm that the function raises a ValueError
    with pytest.raises(ValueError):
        calc_angle(0, 0, 0, 0)
    print("Function successfully raises a ValueError when two identical points are supplied as arguments.")

    #Test to confirm that the function returns 0 when given a point on the positive x axis.
    assert calc_angle(0, 0, 1, 0) == 0
    print("Function generates the correct angle when point 2 is on the positive x axis.")

    #Test to confirm that the function returns 90 when given a point on the positive y axis.
    assert calc_angle(0, 0, 0, 1) == 90
    print("Function generates the correct angle when point 2 is on the positive y axis.")

    #Test to confirm that the function returns 180 when given a point on the negative x axis.
    assert calc_angle(0, 0, -1, 0) == 180
    print("Function generates the correct angle when point 2 is on the negative x axis.")

    #Test to confirm that the function returns -90 when given a point on the negative y axis.
    assert calc_angle(0, 0, 0, -1) == -90
    print("Function generates the correct angle when point 2 is on the negative y axis.")

    #Test to confirm that the function returns 45 when given a point in the first quadrant.
    assert calc_angle(0, 0, 1, 1) == 45
    print("Function generates the correct angle when point 2 is in the first quadrant.")

    #Test to confirm that the function returns 135 when given a point in the second quadrant.
    assert calc_angle(0, 0, -1, 1) == 135
    print("Function generates the correct angle when point 2 is in the second quandrant.")

    #Test to confirm that the function returns -135 when given a point on the third quadrant.
    assert calc_angle(0, 0, -1, -1) == -135
    print("Function generates the correct angle when point 2 is in the third quadrant.")

    #Test to confirm that the function returns -45 when given a point in the fourth quadrant.
    assert calc_angle(0, 0, 1, -1) == -45
    print("Function generates the correct angle when point 2 is in the fourth quadrant.")

    print("All tests passed successfully!")

    
test_calc_angle()

"""
 Make a modified version of your 2D distance calculation script, except that this time the user supplies the following information 
 o First x position o First y position 
 o Distance to the second point 
 • Your script should then calculate an x/y position which would fall that distance from the first point.  
 Since there are a large number of points which would fit these criteria you will need to use a method from the random package to select a suitable random point. 
 • Your script should print out the final result and explain its working. 
"""

def calc_point(x1, y1, dist):
    angle = random.uniform(-180, 180)
    x2 = dist * cos(radians(angle))
    y2 = dist * sin(radians(angle))
    print(f"""The point ({x2}, {y2}) lies at a distance {dist} from point 
      ({x1}, {y1}), and the line between ({x1}, {y1}) and ({x2}, {y2})
      lies at an angle of {angle} degrees from the horizontal line on the
      positive side of x-coordinate {x1}.""")

calc_point(1, 1, 5)