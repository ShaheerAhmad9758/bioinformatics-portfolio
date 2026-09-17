# Rosalind: Complementing a Strand of DNA
# Returns the reverse complement of a DNA sequence

def get_complement(base):
    if base == "A":
        return "T"
    elif base == "C":
        return "G"
    elif base == "G":
        return "C"
    elif base == "T":
        return "A"

def get_reverse_complement(sequence):
    result = ""
    for base in sequence:
        partner = get_complement(base)
        result = result + partner
    return result[::-1]

sequence = "CGATGA"
print(get_reverse_complement(sequence))