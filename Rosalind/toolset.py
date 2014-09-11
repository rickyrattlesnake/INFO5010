import re
DNANucleotides = ('A','C','G','T')
RNANucleotides = ('A','C','G','U')

RNACodonTable = {
         "UUU" : "F" , "CUU" : "L" , "AUU" : "I" , "GUU" : "V"
         , "UUC" : "F" , "CUC" : "L" , "AUC" : "I" , "GUC" : "V"
         , "UUA" : "L" , "CUA" : "L" , "AUA" : "I" , "GUA" : "V"
         , "UUG" : "L" , "CUG" : "L" , "AUG" : "M" , "GUG" : "V"
         , "UCU" : "S" , "CCU" : "P" , "ACU" : "T" , "GCU" : "A"
         , "UCC" : "S" , "CCC" : "P" , "ACC" : "T" , "GCC" : "A"
         , "UCA" : "S" , "CCA" : "P" , "ACA" : "T" , "GCA" : "A"
         , "UCG" : "S" , "CCG" : "P" , "ACG" : "T" , "GCG" : "A"
         , "UAU" : "Y" , "CAU" : "H" , "AAU" : "N" , "GAU" : "D"
         , "UAC" : "Y" , "CAC" : "H" , "AAC" : "N" , "GAC" : "D"
         , "UAA" : "Stop" , "CAA" : "Q" , "AAA" : "K" , "GAA" : "E"
         , "UAG" : "Stop" , "CAG" : "Q" , "AAG" : "K" , "GAG" : "E"
         , "UGU" : "C" , "CGU" : "R" , "AGU" : "S" , "GGU" : "G"
         , "UGC" : "C" , "CGC" : "R" , "AGC" : "S" , "GGC" : "G"
         , "UGA" : "Stop" , "CGA" : "R" , "AGA" : "R" , "GGA" : "G"
         , "UGG" : "W" , "CGG" : "R" , "AGG" : "R" , "GGG" : "G"
         }

def buildFastaRecord(filename):
    fastaRec = {}
    with open(filename, 'rU') as f:
        for line in f:
            if line[0] == '>':
                line = line[1:].rstrip()
                fastaRec[line] = ""
                lastID = line
            else:
                fastaRec[lastID] = fastaRec[lastID] + line.strip()
    return fastaRec

def RNA2Protein(s):
    pString = ""
    for i in range(0,len(s), 3):
        if i+3 <= len(s):
            protein = RNACodonTable[s[i:i+3]]
            if protein == "Stop":
                break
            else:
                pString += protein
    return pString

def findAllSubstrings(s, sub):
    return [m.start() + 1 for m in re.finditer('(?='+sub+')', s)]

def buildProfileMatrix(nucleotides, sList):
    profile = {}
    for n in nucleotides:
        profile[n] = [0] * len(sList[0])
    for s in sList:
        for i in range(0,len(s)):
            profile[s[i]][i] += 1
    return profile

def findConcensus(nucleotides, profile):
    concensus = ""
    for i in range(0, len(profile[nucleotides[0]])):
        nuc = nucleotides[0]
        maxNum = 0
        for n in nucleotides:
            if profile[n][i] > maxNum:
                nuc = n
                maxNum = profile[n][i]
        concensus += nuc
    return concensus

def fibonnaci(i):
    prev, curr = 1,1
    if(i == 1 or i == 2):
        return 1
    for i in range(3, i+1):
        prev, curr = curr, prev + curr
    return curr

def mortalFib(n, dRate):
    hist = [fibonnaci(i) for i in range(1,dRate + 1)]
    #One death in the first two death generations
    for i in range(0,2):
        curr = hist[-1] + hist[-2] - 1
        hist.append(curr)
    #No pattern case
    if n <= dRate + 2:
        return hist[n-1]
    #Recursive pattern case
    for i in range(dRate+3, n+1):
        curr = hist[-1] + hist[-2] - hist[-(dRate+1)]
        hist = hist[1:]
        hist.append(curr)
    return hist[-1]

#Read in a text file
fname = "rosalind_cons.txt"
n = 92
d = 20
print(mortalFib(n, d))
