import sys
import copy
from collections import deque
sys.setrecursionlimit(10**6)

M, N, H = list(map(int, input().split(" ")))
crates = []

for h in range(H):
    crates.append([])
    for _ in range(N):
        crates[h].append(list(map(int,input().split(" "))))

def solve(H, N, M, crates):
    q = deque()
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if crates[h][n][m] == 1:
                    q.append((h, n, m))

    dirs = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)]
    while q:
        cur = q.popleft()
        curH, curN, curM = cur[0], cur[1], cur[2]
        for d in dirs:
            nxtH, nxtN, nxtM = curH + d[0], curN + d[1], curM + d[2]
            if nxtH >= H or nxtN >= N or nxtM >= M or nxtH < 0 or nxtN < 0 or nxtM < 0 or \
                crates[nxtH][nxtN][nxtM] != 0:
                continue
            crates[nxtH][nxtN][nxtM] = crates[curH][curN][curM] + 1
            q.append((nxtH, nxtN, nxtM))

    time = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if crates[h][n][m] == 0:

                    return -1
                time = max(time, crates[h][n][m])

    return time - 1

print(solve(H, N, M, crates))