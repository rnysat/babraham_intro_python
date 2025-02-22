"""
Text alignment 
• Write a script which uses 5 input statements to ask the user for 5 names and stores them in 5 separate variables 
• After collecting the names print them out, one per line, using the center method of strings to center them within a 40 character block 

o Make sure that the names are all in uppercase (upper method), and make sure that any spaces have been removed from the ends of the names (strip method) 
• At the bottom of the list add the total length of all of the names which were entered. 
o You will need to use the len function to get the lengths of the names which you can then add together. 
"""
input_1 = input("Enter the first name: ")
input_2 = input("Enter the second name: ")
input_3 = input("Enter the third name: ")
input_4 = input("Enter the fourth name: ")
input_5 = input("Enter the fifth name: ")

string_list = [input_1, input_2, input_3, input_4, input_5]

total_characters = 0
for i in string_list:
    strip_i = i.strip()
    total_characters += len(strip_i)
    print(strip_i.upper().center(40))
print(str(total_characters).center(40))
