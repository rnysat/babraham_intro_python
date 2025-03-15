#Exercise 3: Iteration and Conditions: Iteration and Looping: Angle Ranges

"""Angle Ranges For the set of integer angles from 0-1800 degrees 
find which ones have a math.sin value of zero. Use a range statement 
to create a for loop through the angles. Because you’re going to be 
calculating small fractional values then an == equality test is not 
reliable, so test for the absolute (abs function) sin value being less 
than 0.01."""


from math import radians
from math import sin

sin_theta_0 = []
for i in range(1801):
    if abs(sin(radians(i)) - 0) < 0.01:
        sin_theta_0.append(i)

print(sin_theta_0)
