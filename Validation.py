############################################################
# Function: DNA Sequence Validation 
############################################################
def validate_sequence(dna_sequence):
    if dna_sequence == "":
          print("Sequence cannot be empty!")
    elif set(dna_sequence) <= {"A","T","C","G"}:
        print("Valid Sequence!")
    else:
        print("Invalid Sequence!")
========================================================================================================================
validate_sequence(dna_sequence)


