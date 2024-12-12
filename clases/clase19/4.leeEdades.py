# 4.leeEdades.py

def leeEdades(nomFich):
    r = {}
    f = open(nomFich)
    for lin in f:
        fil, eds = lin.split(':')
        nac, mue = eds.split('a')
        nac = int(nac)
        mue = int(mue)
        r[fil] = nac - mue
    return r


# ----------
fil = leeEdades('filosofos.txt')
print(fil)


