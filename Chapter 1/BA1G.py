#Compute the Hamming Distance Between Two Strings
def hamming_distance(p, q):
    if len(p) != len(q):
        return -1
    br = 0
    for i in range(0, len(p)):
        if (p[i] != q[i]):
            br = br + 1
    return br


if __name__ == "__main__":
    p = "GGGCCGTTGGT"
    q = "GGACCGTTGAC"

    res = hamming_distance(p, q)
    print(res)
