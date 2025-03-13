#Exercise 2: Data Structure: Random Data

"""Make an empty list and then populate it with 10 numbers drawn 
from a normal distribution with a mean (mu) of 10 and a standard 
deviation (sigma) of 3 Calculate the mean, standard deviation and 
standard error of the mean of the simulated data. 

You can import random then use the random.normalvariate function 
to get the random values. You can import statistics then use
statistics.mean and statistics.stdev to calculate those values.  

For the SEM you need to divide the SD by the square root (math.sqrt) 
of the number of data points (len of the list) minus one. """

import random
import statistics
import math

norm_data = []

for i in range(10):
    norm_data.append(random.normalvariate(mu = 10, sigma = 3))

norm_mean = statistics.mean(norm_data)
norm_stdev =statistics.stdev(norm_data) 
norm_sem = norm_stdev/(math.sqrt(len(norm_data)-1))

print(f"The mean of the simulated data is {norm_mean}")
print(f"The standard deviation of the simulated data is {norm_stdev}")
print(f"The standard error of the mean of the simulated data is {norm_sem}")

