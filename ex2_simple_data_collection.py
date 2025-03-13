#Exercise 2: Data Structures: Lists and Dictionaries: Simple Data Collection
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