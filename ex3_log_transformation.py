#Exercise 3: Iteration and Conditions: Iteration and Looping: Log transformation

"""Create a random 2D dataset of 10 rows and 10 columns using nested 
lists.  Populate it with random values between 1 and 1,000,000. 

Start with an empty list then use two nested for loops using range(10) to 
append a new list and append math.randint() values into it. Log transform 
the data by iterating over the original data structure and building a new 
one.  Again this will be two for loops, one to go through the 10 lists, 
and the second to go through the 10 values in each list.  

Reduce the precision of the log transformed values to 1 decimal place 
using round. Print out the transformed data. """

import random
import math

data_2d = []
for i in range(10):
    data_2d.append([])
    for j in range(10):
        data_2d[i].append(random.randint(1, 1000000))

data_2d_log = []
for i in range(10):
    level_1= data_2d[i]
    data_2d_log.append([])
    for j in range(10):
        level_2 = level_1[j]
        data_2d_log[i].append(round(math.log10(level_2), 1))

print(data_2d_log)