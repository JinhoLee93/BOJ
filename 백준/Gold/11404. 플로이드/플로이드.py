import sys

N = int(input())
M = int(input())
paths = []
for _ in range(M):
    paths.append(list(map(int, input().split(" "))))

def solve():
    distMap = [[float("inf") for _ in range(N)] for _ in range(N)]

    for p in paths:
        src, dest, cost = p[0] - 1, p[1] - 1, p[2]
        distMap[src][dest] = min(distMap[src][dest], cost)

    for i in range(N):
        distMap[i][i] = 0

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if distMap[j][i] != float("inf") and distMap[i][k] != float("inf"):
                    distMap[j][k] = min(distMap[j][k], distMap[j][i] + distMap[i][k])

    for i in range(N):
        for j in range(N):
            if distMap[i][j] == float("inf"):
                distMap[i][j] = 0

    return distMap

res = solve()
for r in res:
    st = [str(s) for s in r]
    print(" ".join(st))
