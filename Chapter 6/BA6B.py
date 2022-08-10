#Compute the Number of Breakpoints in a Permutation
def Breakpoints(P):
    bpoints = [0] + P + [len(P) + 1]
    br = 0
    for i in range(len(P) + 1):
        if (bpoints[i + 1] - bpoints[i] != 1):
            br += 1
    return br


if __name__ == "__main__":
    x = '''(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)'''
    P = list(map(int, x[1:-1].split(" ")))
    res=Breakpoints(P)
    print(res)