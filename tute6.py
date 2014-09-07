import sys
sys.setrecursionlimit(100000)

m = 5
n = 3

def findNumPaths(m, n):
    pathNums = [[1]+[0]*(m-1) if i !=0 else [1]*m for i in range(0,n)]
    # print(pathNums)
    for j in range(1,n):
        for i in range(1,m):
            pathNums[j][i] = pathNums[j][i-1] + pathNums[j-1][i-1] + pathNums[j-1][i]
    # print(pathNums)
    return pathNums[n-1][m-1]

print(findNumPaths(m,n))
