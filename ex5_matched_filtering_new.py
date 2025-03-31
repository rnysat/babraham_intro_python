from pathlib import Path
import re

file_path = r"C:\Users\Documents\babraham_intro_python\babraham_intro_python"
re_fp = re.sub(r"\\", r"/", file_path)

fp = Path(re_fp)

stats = "statistical_hits.txt"
genes = "genome_annotation.txt"

gene_dict = {}
gene_stat_dict = {}

with open(fp.joinpath(genes), "rt", encoding = "UTF-8") as f:
    for line in f:
        gene = line.split("\t")[0]
        gene_dict[gene] = line.strip("\n")

with open(fp.joinpath(stats), "rt", encoding = "UTF-8") as f:
    for line in f:
        gene = line.split("\t")[0]
        output = "\t".join(line.split("\t")[1:]).strip("\n")
        gene_stat_dict[gene] = f"{gene_dict[gene]}\t{output}"

with open(fp.joinpath("matched_filtering.txt"), "wt", encoding = "UTF-8") as f:

    for key, value in gene_stat_dict.items():
        print(value, file = f)
