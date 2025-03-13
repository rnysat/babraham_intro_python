#Exercise 2: Data Structure: Random Genomic Position

import random

chr_name_list = [f"chr{i}" for i in range(1, 23)]
sex_chr_list = ["chrX", "chrY"]
chr_name_list.extend(sex_chr_list)
chr_name_choice = random.choice(chr_name_list)

chr_len_list = [
248956422,
242193529,
198295559,
190214555,
181538259,
170805979,
159345973,
145138636,
138394717,
133797422,
135086622,
133275309,
114364328,
107043718,
101991189,
90338345,
83257441,
80373285,
58617616,
64444167,
46709983,
50818468,
156040895,
57227415]

chr_name_len_dict = dict(zip(chr_name_list, chr_len_list))

chr_len_choice = chr_name_len_dict[chr_name_choice]

pos_choice = random.randint(0, chr_len_choice)


strand_tuple = ("+", "-")
strand_choice = random.choice(strand_tuple)

print(f"{chr_name_choice}:{strand_choice}:{pos_choice}")