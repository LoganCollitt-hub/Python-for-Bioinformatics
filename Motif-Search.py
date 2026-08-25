############################################################
# Function: Motif Search
############################################################
# Function to find DNA motif
def find_motif(dna_sequence, motif):
# Initializes an empty list to store the starting indices where the motif is found (zero-based).
    zero_based=[]
# Iterates through the DNA sequence and checks each position for a matching motif.
    for i in range(len(dna_sequence) - len(motif)+1):
# Extracts a segment of the DNA sequence equal in length to the motif.
        if dna_sequence[i:i+len(motif)] == motif:
# If a match is found, adds the current starting index to the list.
            zero_based.append(i)
# Converts zero-based positions into one-based positions.
    one_based = [i + 1 for i in zero_based]
# Calculates the distance between each consecutive motif occurrence.
    distances = [zero_based[i+1] - zero_based[i]for i in range(len(zero_based) - 1)]
# Finds the shortest and longest distances between motif occurrences.
    shortest = min(distances)
    longest = max(distances)

    return zero_based, one_based, distances, shortest, longest
============================================================================================================
# Defines a smotif to search for.
motif = "ATG"
zero_based, one_based, distances, shortest, longest = find_motif(dna_sequence,motif)

print(f"Motif: {motif}")
print(f"Count: {len(zero_based)}")

# Converts each value into string format for printing.
print(f"Zero based: {','.join(str(x) for x in zero_based)}")
print(f"One based: {','.join(str(x) for x in one_based)}")
print(f"Distances: {','.join(str(x) for x in distances)}")
print(f"Shortest: {shortest}")
print(f"Longest: {longest}")
