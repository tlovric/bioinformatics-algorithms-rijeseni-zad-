#Implement ChromosomeToCycle
def ChromosomeToCycle(chromosome):
    cycle = []
    for j in range(0, len(chromosome)):
        i = int(chromosome[j])
        if i > 0:
            cycle.append(2 * i - 1)
            cycle.append(2 * i)
        else:
            cycle.append(-2 * i)
            cycle.append(-2 * i - 1)
    return cycle


if __name__ == "__main__":
    x='''(+1 -2 -3 +4)'''
    chromosome = x[1:-1].split(" ")
    res = ChromosomeToCycle(chromosome)

    for i in range(len(res)):
        res[i] = str(res[i])
    res = " ".join(res)
    res = "(" + res + ")"
    print(res)