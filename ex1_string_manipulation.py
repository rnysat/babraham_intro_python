"""
Organism names 

• Write a script to correctly format organism scientific names (eg Homo sapiens). 

o It should interactively ask for the Genus (eg homo) and Species (eg sapiens) using input() statements 
o It should then print out the name with the Genus with an uppercase initial letter and the species all in lowercase. 
o Look at the capitalize and lower methods in the str class to do these transformations. 
https://docs.python.org/3/library/stdtypes.html#textseq  
"""
genus = input("Enter the Genus of the organism of interest: ")
species = input("Enter the Species of the organism of interest: ")

print(f"The organism of interest is: {genus.title()} {species.lower()}")