#Generate the Theoretical Spectrum of a Cyclic Peptide
def TheoreticalSpectrum(peptide):
    mass = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }

    res = []
    extended_peptide = peptide + peptide[:-1]
    for i in range(len(peptide)):
        for j in range(1, len(peptide)):
            substring = extended_peptide[i:i + j]
            res.append(sum([mass[x] for x in substring]))

    res.append(0)
    res.append(sum([mass[x] for x in peptide]))

    return map(str, sorted(res))

if __name__ == "__main__":
    inlines = input()
    res=TheoreticalSpectrum(inlines)
    print(" ".join(res))
