"""Create a data structure to hold the following genomic positions taken from the human GRCh38 genome. 

Chr1:90435481-90535480 
Chr4:121080701-121180700 
Chr5:58203396-58303395 
Chr6:24011285-24111284 
Chr7:27397324-27497323 
Chr9:63677076-63777075 
Chr12:57831538-57931537 
Chr13:80438618-80538617 
Chr16:86177236-86277235 
Chr18:39459388-39559387 

Use the code you wrote in last week’s exercise to generate random genomic positions, 
only this time use a loop to generate positions and check them to see if they fall into any of the list of regions above.  
Count how many times you hit each region.  
Stop when any of the regions has 10 hits in it. 
Finish by printing the number of hits you got to each region, 
and the total number of random positions you had to generate to achieve this."""

import random

chr_names = ["chr"+str(i) for i in [1, 4, 5, 6, 7, 9, 12, 13, 16, 18]]
start_pos = [90435481, 121080701, 58203396, 24011285, 27397324, 63677076, 57831538, 80438618, 86177236, 39459388]
stop_pos = [90535480, 121180700, 58303395, 24111284, 27497323, 63777075, 57931537, 80538617, 86277235, 39559387]

grc_h38 = {k:{} for k in chr_names}

for i, k in enumerate(grc_h38.keys()):
    grc_h38[k]["start_pos"] = start_pos[i]
    grc_h38[k]["stop_pos"] = stop_pos[i]

chr_len_list = [248956422, 242193529, 198295559, 190214555, 181538259, 170805979, 159345973, 145138636, 138394717,
133797422, 135086622, 133275309, 114364328, 107043718, 101991189, 90338345, 83257441, 80373285, 58617616, 64444167,
46709983, 50818468, 156040895, 57227415]

def rand_chr_gen():
    chr_name_list = [f"chr{i}" for i in range(1, 23)]
    sex_chr_list = ["chrX", "chrY"]
    chr_name_list.extend(sex_chr_list)
    chr_name_choice = random.choice(chr_name_list)


    chr_name_len_dict = dict(zip(chr_name_list, chr_len_list))
    chr_len_choice = chr_name_len_dict[chr_name_choice]
    pos_choice = random.randint(0, chr_len_choice)
    
    strand_tuple = ("+", "-")
    strand_choice = random.choice(strand_tuple)
    return f"{chr_name_choice}:{strand_choice}:{pos_choice}"

for k, v in grc_h38.items():
    v["hit_count"] = 0

def check_10():
    count_list = []
    for v in grc_h38.values():
        count_list.append(v["hit_count"])
    return max(count_list)

counter = 0
while check_10() < 10:
    name, strand, pos = rand_chr_gen().split(":")
    try:
        if (int(pos) >= grc_h38[name]["start_pos"]) and (int(pos) <= grc_h38[name]["stop_pos"]):
            grc_h38[name]["hit_count"] += 1
    except KeyError:
        continue
    counter +=1

for k, v in grc_h38.items():
    print(f"""The region between bases {v["start_pos"]} and {v["stop_pos"]} 
          on chromosome {k} received {v["hit_count"]} hits.""")

print(f"{counter} random positions had to be generated to achieve this.")