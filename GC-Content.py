def calculate_gc_content (dna_sequence):
    freq = nucleotide_frequency(dna_sequence)
# Retrieves the nucleotide counts and extracts the combined total of G and C bases.
    gc_count = freq["G"] + freq["C"]
# Calculates GC content by dividing the GC count by the total sequence length.
    gc_content = (gc_count / len(dna_sequence)) * 100
    print(f"GC content is: {gc_content:.2f}%")
