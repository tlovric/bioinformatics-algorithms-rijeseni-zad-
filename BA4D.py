#Compute the Number of Peptides of Given Total Mass
def get_all_combinations(mass, aa_masses, counter):
    if (mass in counter):
        return counter[mass]

    if mass < 0:  # znaci
        return 0

    if mass == 0:
        return 1

    counter[mass] = 0
    for mass_ in aa_masses:
        counter[mass] += get_all_combinations(mass - mass_, aa_masses, counter)

    return counter[mass]


def GivenMassProblem(mass):
    amino_acid_mass = {
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

    counter = {}
    aa_masses=set(amino_acid_mass.values())
    return get_all_combinations(mass, aa_masses, counter)  # pazi,ovde ide set jer dva imaju isto

if __name__ == "__main__":
    inlines = int(input())
    res=GivenMassProblem(inlines)
    print(res)