############################################################
# Function: Motif Search
############################################################

def find_motif(dna_sequence, motif):
    zero_based=[] 
    for i in range(len(dna_sequence) - len(motif)+1):
        if dna_sequence[i:i+len(motif)] == motif:
            zero_based.append(i)
    one_based = [i + 1 for i in zero_based]
    distances = [zero_based[i+1] - zero_based[i]for i in range(len(zero_based) - 1)]

    shortest = min(distances)
    longest = max(distances)

    return zero_based, one_based, distances, shortest, longest
========================================================================================================================
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
