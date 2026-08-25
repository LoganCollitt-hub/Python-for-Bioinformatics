!pip install biopython
from Bio.Seq import Seq
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

'''
========================================
             END OF PROGRAM
========================================
'''
