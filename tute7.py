import math
filename = "test1.txt"
fastaRec = {}

with open(filename, 'rU') as f:
    for line in f:
        if line[0] == '>':
            line = line[1:].rstrip()
            fastaRec[line] = ""
            lastID = line
        else:
            fastaRec[lastID] = fastaRec[lastID] + line.strip()
#print(fastaRec)


def findKmers(fastaRec, k):
    for seqId in fastaRec:
        kMers = {}
        seq = fastaRec[seqId]
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            if kmer in kMers:
                kMers[kmer] += 1
            else:
                kMers[kmer] = 1
        fastaRec[seqId] = (seq, kMers)

def findLength(seqID):
    kmers = fastaRec[seqID][1]
    total = 0
    for k in kmers:
        total += kmers[k]**2
    return math.sqrt(total)

def findCosine(seqId1, seqId2):
    total = 0

    for k in fastaRec[seqId1][1]:
        if k in fastaRec[seqId2][1]:
            total += fastaRec[seqId1][1][k] * fastaRec[seqId2][1][k]

    return total / (findLength(seqId1) * findLength(seqId2))

def findDistance(seqId1, seqId2):
    return 1 - findCosine(seqId1, seqId2)

def findPairwiseDistance(fastaRec):
    distMap = []
    for i in fastaRec:
        for j in fastaRec:
            distMap.append((i, j, findDistance(i, j)))
    return distMap


(fastaRec, 2)
seqId1, seqId2 = list(fastaRec.keys())
print(seqId1, seqId2)
findKmers(fastaRec, 3)
# print(fastaRec)
print("***********************")
# print(findCosine(seqId1, seqId2))
# print(findDistance(seqId1, seqId2))
print(findPairwiseDistance(fastaRec))



