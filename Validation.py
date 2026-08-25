#Example DNA Sequence
dna_sequence = (
    "ATGCGTACGTTAGCTAGCGATCGATGCTAACGTTAGCGGATCCATGAACTGCTAGCTAACGATCGTACG"
    "ATGCCGTTAGCATCGATGCTAGGCTAACCGATCGTACGATGAACTAGCTAGCGTACCGATGCTAACGT"
    "TAGCGATCCGATGAACTGCTAGCATGCGTACGTTAGCTAACGATCGGCTAGCTAGCATGAACTGCGTA"
    "CCGATGCTAACGTTAGCGATCGATGCCGTTAGCTAGCATGAACTGCTAACCGATCGTACGATGCTAG"
    "CTAGCGTTAGCATGCGTACGATCGATGAACTGCTAGCTAACGTTAGCGATCCGATGCTAGCATGAACT"
    "GCGTACCGATGCTAACGTTAGCTAGCGATCGATGCCGTTAGCATGAACTGCTAGCTAACCGATCGTAC"
)

=========================================================================================
=========================================================================================
# Converts the sequence to uppercase to ensure consistent processing.
dna_sequence = dna_sequence.upper().replace('',"")

# Defines a function that checks each base in the DNA sequence.
def validate_sequence(dna_sequence):
# Check if the sequence is empty
    if dna_sequence == "":
          print("Sequence cannot be empty!")
    elif set(dna_sequence) <= {"A","T","C","G"}:
# If all characters in the sequence are valid nucleotides, the sequence is accepted.
        print("Valid Sequence!")
    else:
# If any character is not a valid nucleotide, the sequence is rejected.
        print("Invalid Sequence!")
=========================================================================================
=========================================================================================
validate_sequence(dna_sequence)


