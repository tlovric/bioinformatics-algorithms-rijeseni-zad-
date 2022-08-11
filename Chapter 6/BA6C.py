#Compute the 2-Break Distance Between a Pair of Genomes
def ColoredEdges(P):
    edges = []
    for kromosom in P:
        nodes = ChromosomeToCycle(kromosom)
        for j in range(1, len(nodes), 2):
            if j != len(nodes) - 1:
                edges.append([nodes[j], nodes[j + 1]])
            else:
                edges.append([nodes[j], nodes[0]])
    return edges


def ChromosomeToCycle(kromosom):
    nodes = []
    for el in kromosom:
        if el > 0:
            nodes.append(2 * el - 1)
            nodes.append(2 * el)
        else:
            nodes.append(-2 * el)
            nodes.append(-2 * el - 1)
    return nodes


def nadi_sljedeci(trenutni, edges):
    if len(edges) == 0:
        return -1
    idx = 0
    while not (trenutni[0] in edges[idx] or trenutni[1] in edges[idx]):
        idx += 1
        if idx == len(edges):
            return -1
    return edges[idx]


def twoBreakDistance(P, Q):
    edgesP = ColoredEdges(P)  # red edges
    edgesQ = ColoredEdges(Q)  # blue edges
    edges = edgesP + edgesQ

    blokovi = set()
    for edge in edges:
        blokovi.add(edge[0])
        blokovi.add(edge[1])

    ciklusi = []

    while len(edges) != 0:
        start = edges[0]
        edges.remove(edges[0])
        ciklus = [start]
        current = nadi_sljedeci(start, edges)
        while current != -1:
            ciklus.append(current)
            edges.remove(current)
            current = nadi_sljedeci(current, edges)
        ciklusi.append(ciklus)
    return len(blokovi) // 2 - len(ciklusi)

if __name__ == "__main__":
    f='''(+1 +2 +3 +4 +5 +6)
(+1 -3 -6 -5)(+2 -4)'''
    P = f.splitlines()[0][1:-1].split(")(")
    Q = f.splitlines()[1][1:-1].split(")(")
    for i in range(len(P)):
        P[i] = [int(el) for el in P[i].split(" ")]
    for i in range(len(Q)):
        Q[i] = [int(el) for el in Q[i].split(" ")]
    print(twoBreakDistance(P, Q))