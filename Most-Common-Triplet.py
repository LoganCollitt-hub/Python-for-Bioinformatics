def most_common_triplet(dna):
    dna = dna.upper().replace(' ', '')
    triplet_count = {}
    for i in range(len(dna) - 2):
        triplet = dna[i:i+3]
        if len(triplet) == 3:
            triplet_count[triplet] = triplet_count.get(triplet, 0) + 1
    if not triplet_count:
        return None, 0
    max_triplet = max(triplet_count, key=triplet_count.get)
    return max_triplet, triplet_count[max_triplet]
