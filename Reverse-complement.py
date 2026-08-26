############################################################
# Function: Get Complement
############################################################
def get_complement(dna_sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    complement_list = [complement_dict[base] for base in dna_sequence]
    return ''.join(complement_list) 
############################################################
# Function: Get reverse complement
############################################################
def get_reverse_complement(dna_sequence):
    complement_list = get_complement(dna_sequence)
    reverse_complement_list = complement_list[::-1]
    reverse_complement = ''.join(reverse_complement_list)
    return reverse_complement
############################################################
complement = get_complement(dna_sequence)
reverse_complement = get_reverse_complement(dna_sequence)
