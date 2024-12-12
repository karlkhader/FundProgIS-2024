# 5.masLongevo.py

def leeEdades(nomFich):
    r: dict = {}
    f = open(nomFich)
    for lin in f:
        fil, eds = lin.split(':')
        nac, mue = eds.split('a')
        nac: int = int(nac)
        mue: int = int(mue)
        r[fil] = nac - mue
    return r

# ... la primera vez
def másMenosLongevo(d):
    M = None
    m = None
    for fil in d:
        if M == None:
            M = d[fil]
            m = d[fil]
        if d[fil] > M:
            R = fil
            M = d[fil]
        elif d[fil] < m:
            r = fil
            m = d[fil]

    return r, R


# ----------
fil = leeEdades('filosofos.txt')
print(másLongevo(fil))
print()
print(másLongevo2(fil))


