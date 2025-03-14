#Exercise 2: Data Structures: Multi Level Data: Amino Acid Properties

"""Make up a data structure of the properties of amino acids.  

The top level should be a dictionary where the keys are the one letter amino acid codes, 
and the values are another dictionary with keys of “long name” and “molecular weight” containing the appropriate values.  

Details of the values can be found here.  
Allow the user to enter a 1 letter amino acid code and have the script print the long name and weight for that amino acid. """

aa_monograph = list("ARNDCEQGHILKMFPSTWYV")


aa_properties = {k:{"long_name":None, "molecular_weight":None} for k in aa_monograph}

aa_long_name = "Alanine Arginine Asparagine Aspartate Cysteine Glutamate Glutamine Glycine Histidine Isoleucine Leucine Lysine Methionine Phenylalanine Proline Serine Threonine Tryptophan Tyrosine Valine".split()
aa_mol_weight = [89.1, 174.2, 132.1, 133.1, 121.2, 147.1, 146.2, 75.1, 155.2, 131.2, 131.2, 146.2, 149.2, 165.2, 115.1, 105.1, 119.1, 204.2, 181.2, 117.1]

for i, v in enumerate(aa_monograph):
    aa_properties[v]["long_name"] = aa_long_name[i]
    aa_properties[v]["molecular_weight"] = aa_mol_weight[i]

user_aa_monograph = input("Enter a 1-letter amino acid code in order to retrieve its long name and molecular weight: ")

print(f"""The 1-letter amino acid code {user_aa_monograph} refers to the amino acid with long name {aa_properties[user_aa_monograph]["long_name"]}
      and molecular weight {aa_properties[user_aa_monograph]["molecular_weight"]} g/mol.""")