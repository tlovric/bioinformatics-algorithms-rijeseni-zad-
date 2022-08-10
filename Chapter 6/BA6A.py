#Implement GreedySorting to Sort a Permutation by Reversals
def k_reversal(P, k):
    if ("+" + str(k + 1) in P):
        ind2 = P.index("+" + str(k + 1)) #vraca poziciju elementa
    else:
        ind2 = P.index("-" + str(k + 1))

    P = P[:k] + ["+" + s[1:] if s[0] == "-" else "-" + s[1:] for s in P[k:(ind2 + 1)]][::-1] + P[(ind2 + 1):]
    return P


def GreedySorting(P):
    s = []
    for k in range(len(P)):
        if P[k] != ("+" + str(k + 1)):
            P = k_reversal(P, k)
            s.append(P)

            if (P[k] == "-" + str(k + 1)):
                P = P[:k] + ["+" + str(k + 1)] + P[(k + 1):] #ovaj u sredini minja predznak ako je clan neg da postane poz
                s.append(P)

    return s


if __name__ == "__main__":
    x = '''(-3 +4 +1 +5 -2)'''
    P = x[1:-1].split(" ") #priskoci zagrade

    res = GreedySorting(P)
    for r in res:
        text = "(" + " ".join(r) + ")"
        print(text)
