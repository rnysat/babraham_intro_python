#Exercise 2: Data Structure: Animal Set
"""Write a script which asks the user to input the names of 5 animals.  
Put each of these into a set.  
Then ask them for a final input and print out a message saying whether
the animal they entered last has been seen before by using the in test.
Make the query case insensitive by converting everything to lower case. 
For the output you can just print True or False – we’ll be able to do 
cleverer things with the data after next week’s session. """

animals = set()

animal1 = input("Enter the name of the first animal: ")
animal2 = input("Enter the name of the second animal: ")
animal3 = input("Enter the name of the third animal: ")
animal4 = input("Enter the name of the fourth animal: ")
animal5 = input("Enter the name of the fifth animal: ")

animals.add(animal1.lower())
animals.add(animal2.lower())
animals.add(animal3.lower())
animals.add(animal4.lower())
animals.add(animal5.lower())

last = input("Enter the name of the final animal:")

print(last.lower() in animals)