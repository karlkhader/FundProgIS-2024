# 1.printMolecula.py

def printChem(molec):
    for ele in molec:
        print(ele[0], end='')
        if ele[1] > 1:
            print(ele[1], end="")
    print()


sulfAcid = [['H', 2], ['S', 1], ['O', 4]]
sosaCaustica = [['Na', 1], ['O', 1], ['H', 1]]
sodSulf = [['Na', 2], ['S', 1], ['O', 4]]
agua = [['H', 2], ['O', 1]]

printChem(sulfAcid)

