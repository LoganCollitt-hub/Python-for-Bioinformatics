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

aa_sorted = dict(sorted(count_amino_acids(protein).items()))
print(f"Amino Acid: {aa_sorted}")
############################################################
# Function: Most common Amino acid 
############################################################
def most_common_aa(aa_sorted):
    highest_count = max(aa_sorted.values())
    for aa in aa_sorted:
        if aa_sorted[aa] == highest_count:
            return aa, highest_count
            
most_common, highest_count = most_common_aa(aa_sorted)
print(f"Most common amino acid: {most_common}")
############################################################
# Function: Amino Acid Composition
############################################################
def amino_comp(protein_sequence):
    aa_counts = count_amino_acids(protein_sequence)
    for aa in protein_sequence:
        aa_percent = (aa_counts[aa] / len(protein_sequence)) * 100
        print(aa, ":", f"{aa_percent:.2f}%")

