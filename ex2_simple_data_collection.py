#Exercise 2: Data Structures: Lists and Dictionaries: Simple Data Collection

"""Write a script which will prompt the user to enter 5 numeric values
using 5 input statements.  

Convert these to numbers using float() and put them into a list.

Use the sort method to order the list then print it. 

Use a list selection using [ ] to pull out and print just the first
(lowest) value in the list. 

Next reverse the sorted list and print it again so you can see the
numbers from highest to lowest.

Have a look at the documentation for the sort method to see how you
could have done the sorting this way initially. 

Finally print out a statement which uses the count method to say how
many times the number 2 was present in the data. """
num_list = []

try:
    input1 = float(input("Enter the first numeric value: "))
    num_list.append(input1)
except ValueError:
    print("""The input you have given for the first value cannot be converted to a float.""")

try:
    input2 = float(input("Enter the second numeric value: "))
    num_list.append(input2)
except ValueError:
    print("""The input you have given for the second value cannot be converted to a float.""")

try:
    input3 = float(input("Enter the third numeric value: "))
    num_list.append(input3)
except ValueError:
    print("""The input you have given for the third value cannot be converted to a float.""")

try:
    input4 = float(input("Enter the fourth numeric value: "))
    num_list.append(input4)
except ValueError:
    print("""The input you have given for the fourth value cannot be converted to a float.""")

try:
    input5 = float(input("Enter the fifth numeric value: "))
    num_list.append(input5)
except ValueError:
    print("""The input you have given for the fifth value cannot be converted to a float.""")

num_list.sort()
print(num_list)
print(num_list[0])
num_list.reverse()
print(num_list)
#num_list.sort(reverse = True)


num_list_str = " ".join([str(x) for x in num_list])
two_count = num_list_str.count("2")
print(f"The number 2 is present in the inputs {two_count} times.")