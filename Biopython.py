!pip install biopython
from Bio.Seq import Seq
========================================================================================================================
############################################################
# Function: DNA Analysis
############################################################
dna = Seq(dna_sequence)
print("DNA Sequence:", repr(dna))
print(f"Length: {len(dna)}")
############################################################
# Function: Transcription
############################################################
rna = dna.transcribe()
trim = len(rna) - (len(rna) % 3)
rna = rna[:trim]
print("RNA Sequence:", repr(rna))
print(f"Length: {len(rna)}")
############################################################
# Function: Translation
############################################################
protein = rna.translate()
print("Protein Sequence:", repr(protein))
print(f"Length: {len(protein)}")

