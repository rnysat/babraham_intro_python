from pathlib import Path
import re

bs = r"C:\Users\rebec\Documents\babraham_intro_python\babraham_intro_python\Mapping Stats"
fs = bs.replace("\\", "/")

file_path = Path(fs)

percent_regex = "\((\d{1,3}\.\d{2}%)\) aligned exactly 1 time"
file_regex = r"Mapping Stats\\(.+)_GRCm38_bowtie2_stats\.txt"

for file in file_path.iterdir():
    with open(file, "rt", encoding = "UTF-8") as f:
        content = " ".join(f.readlines())
        percent = re.search(percent_regex, content)
        if percent != None:
            fn = re.search(file_regex, str(file)).groups(1)[0]
            p = percent.groups(1)[0]
            print(f"The file {fn} has {p} of reads that aligned exactly once.")



