#Find an Eulerian Cycle in a Graph
def EulerianCycle(D):
    pocetni_cvor=list(D.keys())[0]
    trenutni_cvor=pocetni_cvor
    konacni_put=[pocetni_cvor]

    while D:
        if trenutni_cvor in D:
            konacni_put.append(D[trenutni_cvor][0])
            if len(D[trenutni_cvor])==1:
                del D[trenutni_cvor]
            else:
                del D[trenutni_cvor][0]
            trenutni_cvor=konacni_put[-1]
        else:
            for i, elem in enumerate(konacni_put):
                if elem in D:
                    novi_ciklus = konacni_put[i: -1] + konacni_put[:i + 1]
                    konacni_put = novi_ciklus
                    trenutni_cvor = elem
                    break

    return konacni_put

if __name__ == "__main__":
    f='''0 -> 3
1 -> 0
2 -> 1,6
3 -> 2
4 -> 2
5 -> 4
6 -> 5,8
7 -> 9
8 -> 7
9 -> 6'''

    graf = {}
    for edge in f.splitlines():
        first, second = edge.split(" -> ")
        second = second.split(",")
        graf[first] = second
    ciklus=EulerianCycle(graf)
    print("->".join(ciklus))