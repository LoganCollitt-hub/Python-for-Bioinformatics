def find_mutation_positions(dna_sequence, target_nucleotide='C'):
    for i, base in enumerate(dna_sequence):
        if base != target_nucleotide: mutation_positions.append(i)
    return mutation_positions

target = "T"
i = 0
current_sequence = ""
longest_sequence = ""
mutation_positions = []
==============================================================================================================
mutation_positions = find_mutation_positions(dna_sequence,'C')
print("Possible mutation positions for 'C':", mutation_positions)
       
