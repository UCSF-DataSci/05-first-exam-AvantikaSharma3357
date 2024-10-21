import argparse

complements = {
    "A":"T", 
    "T": "A",
    "G":"C",
    "C": "G"
}

def complement(sequence):
    complement_sequence = ""
    sequence = sequence.upper()
    for nucleotide in sequence:
        complement_sequence += complements[nucleotide]
    return complement_sequence
        
def reverse(sequence):
    sequence = sequence.upper()
    reverse_sequence = sequence[::-1] 
    return reverse_sequence

def reverse_complement(sequence):
    return complement(reverse(sequence))

parser = argparse.ArgumentParser()
parser.add_argument("sequence")
args = parser.parse_args()
sequence = args.sequence 

print("Orignal sequence: ", sequence)
print("Complement: ", complement(sequence))
print("Reverse: ", reverse(sequence))
print("Reverse complement: ", reverse_complement(sequence))


