from pathlib import Path

file_path = Path("C:/Users/X/Documents/babraham_intro_python/babraham_intro_python/")

for file in file_path.iterdir():
    if str(file).endswith(".csv"):
        print(f"The file saved at path {file} has size {file.stat().st_size} in bytes.")
        