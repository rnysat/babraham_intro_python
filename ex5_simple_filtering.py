from pathlib import Path

path_stem = Path("C:/Users/rebec/Documents/babraham_intro_python/babraham_intro_python")
file_path = path_stem.joinpath("cancer_stats.csv")

if not file_path.exists():
    raise FileNotFoundError(f"File could not be found at path {file_path}")

new_file_path = path_stem.joinpath("output_cancer_stats.csv")

with open(file_path, "rt", encoding = "UTF-8" ) as f:
    with open(new_file_path, "wt", encoding = "UTF-8") as f2:
        for index, line in enumerate(f):
            if index == 0:
                print(line, file = f2)
                continue
            values = line.strip().split(",")
            if "NA" in values[2:]:
                break
            female_survival = (float(values[-3])- float(values[-1]))/float(values[-3])
            male_survival = (float(values[-4])- float(values[-2]))/float(values[-4])
            if female_survival > male_survival:
                print(line.strip(), file = f2)
