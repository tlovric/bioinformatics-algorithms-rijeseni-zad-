#Find the Length of a Longest Path in a Manhattan-like Grid
def Manhattantourist(n, m, down, right):
    s = []
    for i in range(n + 1):
        s.append((m + 1) * [0])

    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + down[i - 1][0]

    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] + right[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1])

    return s[n][m]


if __name__ == "__main__":
    x = '''4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2'''
    inlines = x.split('\n')
    n=int(inlines[0].split()[0])
    m=int(inlines[0].split()[1])

    down = []
    for i in range(n):
        down.append([int(x) for x in inlines[1 + i].split()])

    right = []
    for i in range(n + 1):
        right.append([int(x) for x in inlines[n + 2 + i].split()])

    res = Manhattantourist(n, m, down, right)

    print(str(res))