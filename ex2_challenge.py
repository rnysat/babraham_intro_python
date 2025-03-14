#Exercise 2: Data Structures: Challenge

"""Tricky challenge (if you have time / motivation!) 
Create a program to simulate a random sequence based on the composition of a reference sequence. 
The inputs to the program should be 
• A reference DNA sequence 
• The length of a random sequence to simulate 

For reasons we’ll come on to you can treat a string such as "GATATCG" as if it was a list for many operations. 
Make your script count and report the number of occurrences of each of the four letters. 
Print out a count for the number of letters which aren’t accounted for by the 4 expected bases. 
Use the random.choices function to make a selection of the requested size from a population which 
reflects the composition of the original sequence.  

Since your original sequence may have non-GATC letters in it, construct a list of weights to use for choices. 
Your script should cope with the input sequence being uppercase, lowercase or a mix of the two. 
It should force the length to be an integer. """

import random

ref_seq = input("Enter a reference DNA sequence: ").upper()

try:
    sim_len = int(input("Enter the length of the random sequence that you would like to simulate: "))
except ValueError:
    print("The value for the sequence length must be an integer")

bases = list("ATCG")

base_count = {}

for i in ref_seq:
    value = base_count.get(i, 0)
    value += 1
    base_count[i] = value

a = base_count["A"]
t = base_count["T"]
c = base_count["C"]
g = base_count["G"]
other = len(ref_seq) - a - t - c - g

print(f"""Within the reference sequence, there are:
      {a} occurrences of base A,
      {t} occurrences of base T, 
      {c} occurrences of base C, 
      {g} occurrences of base G,
      and {other} occurences of letters that are not accounted for by 
      those 4 bases.   
      """)

sim_seq = random.choices(population = bases, weights = [base_count[i] for i in bases], k = sim_len)

print(f"""The simulated sequence that contains DNA bases in 
      the same proportion as the reference sequence is: {sim_seq}.""")
