from enum import Enum

class Zygosity(Enum):
    homoDom = 1
    hetero = 2
    homoRec = 3


#Read the input
ins = "2 2 2"
k ,m, n = ins.split()

def probPhenotypeExp(g1, g2):
    if g1 == Zygosity.homoDom or g2 == Zygosity.homoDom:
        return 1
    elif g1 == Zygosity.hetero:
        if g2 == Zygosity.hetero:
            return 0.75
        else:
            return 0.5
    else:
        if g2 == Zygosity.hetero:
            return 0.5
        else:
            return 0

def prob2Pop(homoDNum, heteroNum, homoRNum):
    args = (homoDNum, heteroNum, homoRNum)
    t2 = sum(args) * (sum(args) - 1)
    probMatrix = [[],[],[]]
    for z in range(3):
        if z == 0:
            p = homoDNum
        elif z == 1:
            p = heteroNum
        else:
            p = homoRNum
        probMatrix[z] = [p * i / t2 if n != z else p * (i-1) / t2 for n,i in enumerate(args)]
    print(probMatrix)

    totalDomChance = 0
    for i,z in enumerate(Zygosity):
        for j,z2 in enumerate(Zygosity):
            totalDomChance += probMatrix[i][j] * probPhenotypeExp(z,z2)
    return totalDomChance

print(prob2Pop(27,24,18))

