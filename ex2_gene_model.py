#Exercise 2: Data Structures: Gene Model

"""Put the information below into a suitable multi-level data structure.  

It probably makes sense to build the top level gene information in one go, and then add the individual transcripts afterwards.  

Gene     
Name Nanog    
Description Nanog homeobox    
Location 
    Chromsome 12    
    Start 7,787,794    
    End 7,799,146    
    Strand Forward        

Transcripts 
Name ID Length Amino Acids  
NANOG-201 ENST00000229307.9 5182 305  
NANOG-202 ENST00000526286.1 870 289  
NANOG-204 ENST00000541267.5 836 186  
NANOG-203 ENST00000526434.2 558 0  

The top level structure will be a dictionary.  
The Location value will be a second dictionary containing the different pieces of location information.  
The Transcripts value will be a list, where each value in the list will be a dictionary containing the different transcript details.  
Use this data structure to pull out the length of the last transcript. """

top_level_keys = ["Name", "Description", "Location", "Transcripts"]
location_keys = ["Chromosome", "Start", "End", "Strand"]
location_values = [12, 7787794, 7799146, "Forward"]

gene_model = {k:None for k in top_level_keys}
gene_model["Name"] = "Nanog"
gene_model["Description"] = "Nanog homeobox"

gene_model["Location"] = dict(zip(location_keys, location_values))

gene_model["Transcripts"] = [{k: None for k in ["Name", "ID", "Length", "Amino Acids"]} for i in range(4)]

transcript_names = "NANOG-201 NANOG-202, NANOG-204 NANOG-203".split()
ids = "ENST00000229307.9 ENST00000526286.1 ENST00000541267.5 ENST00000526434.2".split()
lengths = [5182, 870, 836, 558]
amino_acids = [305, 289, 186, 0]

for i in range(4):
    gene_model["Transcripts"][i]["Name"] = transcript_names[i]
    gene_model["Transcripts"][i]["ID"] = ids[i]
    gene_model["Transcripts"][i]["Length"] = lengths[i]
    gene_model["Transcripts"][i]["Amino Acids"] = amino_acids[i]

length_last_transcript = gene_model["Transcripts"][-1]["Length"]

print(length_last_transcript)