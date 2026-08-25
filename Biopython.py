!pip install biopython
from Bio.Seq import Seq

def count_amino_acids(protein_sequence):
    # Initializes a dictionary to store the count for each amino acid.
    aa_counts = {}
    for aa in protein_sequence:
        # If the amino acid already exists, increment its count; otherwise start at 1.
        aa_counts[aa] = aa_counts.get(aa, 0) + 1
    return aa_counts

# Defines a function that returns the amino acid with the highest count.
def most_common_aa(aa_sorted):
    # Finds the highest count value in the dictionary.
    highest_count = max(aa_sorted.values())
# Iterates through the dictionary to find the amino acid with the highest count.
    for aa in aa_sorted:
        if aa_sorted[aa] == highest_count:
            return aa, highest_count

'''
========================================
             START OF PROGRAM
========================================
'''

# Converts the standard Python string DNA sequence into a Biopython Seq object.
print("\n======= DNA Sequence Analysis =======\n")
dna = Seq(dna_sequence)
print("DNA Sequence:", repr(dna))
print(f"Length: {len(dna)}")

# Transcribes the DNA sequence into RNA and trims any leftover bases that do not form a complete codon.
print("\n======= Transcription =======\n")
rna = dna.transcribe()
trim = len(rna) - (len(rna) % 3)
rna = rna[:trim]
print("RNA Sequence:", repr(rna))
print(f"Length: {len(rna)}")

# Translates the RNA sequence into a protein sequence.
print("\n======= Translation =======\n")
protein = rna.translate()
print("Protein Sequence:", repr(protein))
print(f"Length: {len(protein)}")

# Sorts the amino acid counts alphabetically.
aa_sorted = dict(sorted(count_amino_acids(protein).items()))

print("\n======= Protein Analysis =======\n")
for aa, count in aa_sorted.items():
    # Prints each amino acid and its count.
    print(f"Amino Acid: '{aa}': {count}")

# Finds the most common amino acid and its count.
print("\n======= Most Common Amino Acid =======\n")
most_common, highest_count = most_common_aa(aa_sorted)

# Calculates the percentage of the most common amino acid relative to the total protein length.
percentage_aa = (highest_count / len(protein)) * 100
print(f"Most common amino acid: {most_common}")
print(f"Percentage: {percentage_aa:.2f}%")

# Counts the number of stop codons in the protein sequence.
print("\n======= Stop Codon Frequency =======\n")
stop_codons = protein.count("*")
print(f"Stop Codon Count: {stop_codons}")

'''
========================================
             END OF PROGRAM
========================================
'''
