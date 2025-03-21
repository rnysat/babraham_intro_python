import re

file_names = """lane1_NoCode_L001_R1.fastq.gz  
lane1_NoIndex_L001_R1.fastq.gz 
lane1_NoIndex_L001_R2.fastq.gz 
pipeline_processing_output.log 
lane7127_ACTGAT_JH25_L001_R1.fastq.gz 
lane7127_ACTTGA_E30_1_2_Hap4_24h_L001_R1.fastq.gz 
lane7127_AGTTCC_JH14_L001_R1.fastq.gz 
lane7127_CGGAAT_JH37_L001_R1.fastq.gz 
lane7127_GCCAAT_E30_1_2l_Hap4_log_L001_R1.fastq.gz 
lane7127_GGCTAC_E30_1_4_Hap4_48h_L001_R1.fastq.gz """


lane_re1 = "lane\d{1,4}"
barcode2 = "[ATCG]{6}"
lane_no_re4 = "L\d{1,3}"
read_no_re5 = "R\d"
file_suffix6 = "[.]fastq[.]gz"

total_regex = f"{lane_re1}_{barcode2}_(.+)_{lane_no_re4}_{read_no_re5}{file_suffix6}"

sample_names = []
for line in file_names.split("\n"):
    ext_group = re.search(total_regex, line)
    if ext_group != None:
        sample_names.append(ext_group.group(1))

print(sample_names)




