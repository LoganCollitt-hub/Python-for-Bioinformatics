def nucleotide_frequency(dna_sequence):
# Initializes a dictionary to store the counts for each of the four standard nucleotides.
    freq = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
# Iterates through each base in the DNA sequence and increments the count for the matching nucleotide.
    for char in dna_sequence:
        freq[char] += 1
    return freq

def nucleotide_percentage(dna_sequence):
# Retrieves the nucleotide frequency dictionary for the given DNA sequence.
    freq = nucleotide_frequency(dna_sequence)
    total_length = len(dna_sequence)
# Calculates the percentage for each nucleotide by dividing its count by the total sequence length.
    for nucleotide, count in freq.items():
       percentage = (count / total_length) * 100
       print(f"Nucleotide percentage of {nucleotide} is:{percentage:.2f}%")

freq = nucleotide_frequency(dna_sequence)
freq_string =','.join(f" {base}:{count}" for base, count in freq.items())
print(f"Nucleotide frequencies:{freq_string}")
