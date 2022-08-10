#Generate the Convolution of a Spectrum
def spectralConvolution(spectrum):
    rez = []
    for x in spectrum:
        for y in spectrum:
            if int(x) > int(y):
                rez.append(int(x) - int(y))
    for i in range(len(rez)): #sortira se po stringu a ne brojevima
        rez[i] = str(rez[i])
    return sorted(rez)


if __name__ == "__main__":
    x='''0 137 186 323'''
    inlines=x.split(" ")
    res = spectralConvolution(inlines)
    print(" ".join(res))