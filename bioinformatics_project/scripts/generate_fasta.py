'''
1. Generate a random DNA sequence of 1 million base pairs (using A, C, G, T).
2. Format the sequence with 80 base pairs per line.
3. Save the sequence in FASTA format in the "data" directory, with the filename "random_sequence.fasta".
'''
import random

nucleotide = ["A","C","G","T"]
sequence_length = 1000000

random_sequence = random.choices(nucleotide,k=sequence_length)

formatted_sequence = ""
for i in range(0, sequence_length, 80):
    formatted_sequence+= ''.join(random_sequence[i:i+80]) + "\n"

filepath = "/Users/avantikasharma/05-first-exam-AvantikaSharma3357/bioinformatics_project/data/random_sequence.fasta" 

with open(filepath, "w") as file:
    file.write(formatted_sequence) 

print(f"Random sequence of length {sequence_length} saved to {filepath}") 