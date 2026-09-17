# Rosalind: Counting DNA Nucleotides
# Counts how many times A, C, G, and T each appear in a DNA sequence

sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

a_count = 0
c_count = 0
g_count = 0
t_count = 0

for base in sequence:
    if base == "A":
        a_count += 1
    elif base == "C":
        c_count += 1
    elif base == "G":
        g_count += 1
    elif base == "T":
        t_count += 1

print(a_count, c_count, g_count, t_count)