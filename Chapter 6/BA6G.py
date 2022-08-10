#Implement CycleToChromosome
def CycleToChromosome(cycle):
    chromosome = []
    for j in range(0, int(len(cycle) / 2)):

        if int(cycle[2 * j]) < int(cycle[2 * j + 1]):
            chromosome.append(int(cycle[2 * j + 1] / 2))
        else:
            chromosome.append(int(-cycle[2 * j] / 2))
    return chromosome


if __name__ == "__main__":
    x='''(1 2 4 3 6 5 7 8)'''
    chromosome = x[1:-1].split(" ") #string
    kop = []
    for x in chromosome:
        kop.append(int(x))
    res = CycleToChromosome(kop)

    for i in range(len(res)):
        if(res[i]>=0):
            res[i] ="+"+ str(res[i])
        else:
            res[i]=str(res[i])
    res = " ".join(res)
    res = "(" + res + ")"
    print(res)