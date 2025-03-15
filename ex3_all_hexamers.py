#Exercise 3: Iteration and Conditions: Iteration and Looping: All hexamers

"""Write a program to collect and print out all 6-mer combinations of the 
DNA bases GATC. There are potentially multiple ways to do this.  

One would be to make a list of the bases then over 6 rounds add each base 
to each position and replace the original list. 

To append a letter to a string you use the + operator, 
so "GA" + "TC" = "GATC""""

bases = "ATCG"

seqs = [""]

for i in range(6):
    editing_seqs = []
    for seq in seqs:
        for base in bases:
            editing_seqs.append(seq+base)
    seqs = editing_seqs

print(seqs)