import csv

# Input the file paths for translation pairs from the grc_eng github repo (https://github.com/kevinkrahn/ancient-greek-datasets)
path_to_grc_eng_files1="/example/path/grc/translation_pairs_a.txt"
path_to_grc_eng_files2="/example/path/eng/translation_pairs_b.txt"

with open(path_to_grc_eng_files1, 'r') as f:
    lines=f.readlines()
    res=[(line.split("\t")[0].replace("\n", "").strip(), line.split("\t")[1].replace("\n", "").strip()) for line in lines]
with open(path_to_grc_eng_files2, 'r') as f:
    lines=f.readlines()
    res.extend([(line.split("\t")[0].replace("\n", "").strip(), line.split("\t")[1].replace("\n", "").strip()) for line in lines])

with open("grc_eng_training_big.csv", "w") as f:
    writer=csv.writer(f)
    writer.writerows(res)
