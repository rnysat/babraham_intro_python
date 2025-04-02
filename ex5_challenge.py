import gzip
from pathlib import Path
import re

gene_name_re = r'gene_name "(.+?)"'
gene_id_re = r'gene_id "(.+?)"'

fp = Path(r"C:\Users\rebec\Documents\babraham_intro_python\babraham_intro_python\Bacteria")

species_dict = {}

for i in fp.iterdir():
    genus_species = " ".join(str(i).split("\\")[-1].split("_")[:2])
    species_dict[genus_species] = {}
    with gzip.open(i, "rt", encoding = "UTF-8") as f:
            gene_lens = {}
            for line in f:
                if len(ll:=line.split("\t")[2:5]) == 3:
                    feature, start, stop = ll
                    if feature.lower() == "gene":
                        gene_len = int(stop) - int(start) + 1
                        if gene_key:=re.search(gene_name_re, line) != None:
                             continue
                        else:
                             gene_key = re.search(gene_id_re, line)
                        gene_lens[gene_key.group(1)] = gene_len
            invert_dict = {length:id for id, length in gene_lens.items()}

            max_gene_len = max(invert_dict.keys())
            max_gene_name = invert_dict[max_gene_len]
            num_genes = len(gene_lens)

            species_dict[genus_species]["gene_count"] = num_genes
            species_dict[genus_species]["longest_gene"] = max_gene_name
            species_dict[genus_species]["longest_gene_length"] = max_gene_len

for k, v in species_dict.items():
     print("\n", k, v, "\n")
help(re.search)