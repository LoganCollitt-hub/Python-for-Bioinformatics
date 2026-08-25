############################################################
# Function: Get Complement
############################################################
def get_complement(dna_sequence):
# Defines a dictionary to map each nucleotide to its complementary base.
    complement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
 # Iterates through each base in the DNA sequence and stores its complement.
    complement_list = [complement_dict[base] for base in dna_sequence]
# Joins the list of complementary bases into a single string.
    return ''.join(complement_list) 
############################################################
# Function: Get reverse complement
############################################################
def get_reverse_complement(dna_sequence):
# Gets the complement of the DNA sequence
    complement_list = get_complement(dna_sequence)
# Reverses the complemented sequence.
    reverse_complement_list = complement_list[::-1]
# Joins the reversed bases into a new string.
    reverse_complement = ''.join(reverse_complement_list)
    return reverse_complement
############################################################
# Calls the complement and reverse complement functions and stores the results.
complement = get_complement(dna_sequence)
reverse_complement = get_reverse_complement(dna_sequence)
