# Rosalind: Counting Point Mutations
# Counts the Hamming distance (number of differing positions) between two equal-length DNA sequences

file = open("rosalind_hamm.fasta", "r")
contents = file.read()
file.close()

lines = contents.splitlines()
seq1 = lines[0]
seq2 = lines[1]

mutations = 0

for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        mutations += 1

print(mutations)