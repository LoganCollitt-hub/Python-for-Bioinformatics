!pip install biopython
from Bio.Seq import Seq
############################################################
#                     START OF PROGRAM                     #
############################################################

print("\n======= DNA Sequence Analysis =======\n")
dna = Seq(dna_sequence)
print("DNA Sequence:", repr(dna))
print(f"Length: {len(dna)}")

############################################################
print("\n======= Transcription =======\n")
rna = dna.transcribe()
trim = len(rna) - (len(rna) % 3)
rna = rna[:trim]
print("RNA Sequence:", repr(rna))
print(f"Length: {len(rna)}")

############################################################
print("\n======= Translation =======\n")
protein = rna.translate()
print("Protein Sequence:", repr(protein))
print(f"Length: {len(protein)}")

############################################################
#                       END OF PROGRAM                     #
############################################################
