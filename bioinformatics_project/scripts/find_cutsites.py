import argparse
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument("fasta_file")
parser.add_argument("cut_site")
args = parser.parse_args()

fasta_file = args.fasta_file
cut_site = args.cut_site

def Read_Fasta(file_path):
    with open(file_path,"r") as file:
        sequence = "".join(line.strip() for line in file)
    return sequence 

def find_cutsite(cut_site,sequence):
    new_cutsite = cut_site.replace("|", "")
    pattern = re.escape(new_cutsite)
    cut_positions = [match.start() for match in re.finditer(pattern,sequence)]
    return cut_positions

def find_cutsite_pairs(cut_positions):
    min_distance = 80000
    max_distance = 120000
    cutsite_pairs = []
    for i in range(len(cut_positions)):
        for j in range(i+1, len(cut_positions)):
            distance = cut_positions[j]-cut_positions[i]
            if min_distance <= distance <= max_distance:
                cutsite_pairs.append((cut_positions[i],cut_positions[j]))
    return cutsite_pairs


sequence = Read_Fasta(fasta_file)
cut_positions = find_cutsite(cut_site,sequence)
cutsite_pairs = find_cutsite_pairs(cut_positions)

print("Analyzing cut site: ", cut_site)
print("Total cut sites found: ", len(cut_positions))
print("Cut site pairs 80-120 kbp apart: ", len(cutsite_pairs))
print("First 5 pairs:")
for i, (start, end) in enumerate(cutsite_pairs[:5]):
    print(f"{i + 1}. {start} - {end}")

output_path = os.path.join("results", "distant_cutsite_summary.txt")
with open(output_path,"w")as file:
    for i, (start,end)in enumerate(cutsite_pairs):
        file.write(f"{i+1}. {start} - {end} \n")


        


