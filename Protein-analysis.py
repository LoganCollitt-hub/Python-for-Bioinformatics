!pip install biopython
from Bio.Seq import Seq
========================================================================================================================
############################################################
# Function: Amino acid count
############################################################
def count_amino_acids(protein_sequence):
    aa_counts = {}
    for aa in protein_sequence:
        aa_counts[aa] = aa_counts.get(aa, 0) + 1
    return aa_counts
############################################################
# Function: Most common Amino acid 
############################################################
def most_common_aa(aa_sorted):
    highest_count = max(aa_sorted.values())
    for aa in aa_sorted:
        if aa_sorted[aa] == highest_count:
            return aa, highest_count
========================================================================================================================
   
aa_sorted = dict(sorted(count_amino_acids(protein).items()))

print("\n======= Protein Analysis =======\n")
for aa, count in aa_sorted.items():
    print(f"Amino Acid: '{aa}': {count}")

print("\n======= Most Common Amino Acid =======\n")
most_common, highest_count = most_common_aa(aa_sorted)
percentage_aa = (highest_count / len(protein)) * 100
print(f"Most common amino acid: {most_common}")
print(f"Percentage: {percentage_aa:.2f}%")

print("\n======= Stop Codon Frequency =======\n")
stop_codons = protein.count("*")
print(f"Stop Codon Count: {stop_codons}")

