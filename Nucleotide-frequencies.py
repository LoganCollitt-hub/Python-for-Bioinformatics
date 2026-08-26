############################################################
# Function: Calculate nucleotide frequency
############################################################
def nucleotide_frequency(dna_sequence):
    freq = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for char in dna_sequence:
        freq[char] += 1
    return freq
############################################################
# Function: Calculate nucleotide percentage
############################################################
def nucleotide_percentage(dna_sequence):
    freq = nucleotide_frequency(dna_sequence)
    total_length = len(dna_sequence)
    for nucleotide, count in freq.items():
       percentage = (count / total_length) * 100
       print(f"Nucleotide percentage of {nucleotide} is:{percentage:.2f}%")
========================================================================================================================
freq = nucleotide_frequency(dna_sequence)
freq_string =','.join(f" {base}:{count}" for base, count in freq.items())
print(f"Nucleotide frequencies:{freq_string}")
nucleotide_percentage(dna_sequence)
