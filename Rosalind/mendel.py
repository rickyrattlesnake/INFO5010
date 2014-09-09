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
    total = homoDNum + heteroNum + homoRNum
    total2 = total * (total - 1)
    homoD_homoD = homoDNum * (homoDNum - 1) / total2
    homoD_hetero = homoDNum * hetero / total2
    homoD_homoR = homoDNum * homoRNum / total2
    homoR_hetero = homoRNum * heteroNum / total2
    homoR_homoR = homoR * (homoR - 1) / total2
    hetero_hetero = hetero * (hetero - 1) / total2
    p = [ i * j / t2 if n != m else i * (j-1) / t2 for n,i in enumerate(args) for m,j in enumerate(args)]
    z2pMap = lambda x, y : (x - 1) * 3 + (y - 1)
    e = [z2pMap(x, y) for x in Zygosity for y in Zygosity]
    print(e)
