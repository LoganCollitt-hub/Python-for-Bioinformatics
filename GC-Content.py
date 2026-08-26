############################################################
# Function: Calculate GC Content
############################################################
def calculate_gc_content (dna_sequence):
    freq = nucleotide_frequency(dna_sequence)
    gc_count = freq["G"] + freq["C"]
    gc_content = (gc_count / len(dna_sequence)) * 100
############################################################
print(f"GC content is: {gc_content:.2f}%")
