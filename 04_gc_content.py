# Rosalind: Computing GC Content
# Finds which sequence in a FASTA file has the highest GC content

def gc_content(seq):
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    for base in seq:
        if base == "A":
            a_count += 1
        elif base == "C":
            c_count += 1
        elif base == "G":
            g_count += 1
        elif base == "T":
            t_count += 1
    return (g_count + c_count) / len(seq) * 100

file = open("rosalind_gc.fasta", "r")
contents = file.read()
file.close()

lines = contents.splitlines()

last_header = None
sequences = {}
for line in lines:
    if line.startswith(">"):
        last_header = line[1:]
        sequences[last_header] = ""
    else:
        sequences[last_header] = sequences[last_header] + line

best_id = None
best_gc = -1

for seq_id, seq in sequences.items():
    percentage = gc_content(seq)
    if percentage > best_gc:
        best_gc = percentage
        best_id = seq_id

print(best_id, best_gc)