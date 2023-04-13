import sys
from collections import deque

def bfs(start, fire):
    q = deque([start])
    visited = set()
    visited.add(start)
    minDist = float("inf")
    dist = 1
    while q:
        f, nf = deque(fire), []
        while f:
            fireR, fireC = f.popleft()
            for d in dirs:
                nfr, nfc = fireR + d[0], fireC + d[1]
                if 0 <= nfr < N and 0 <= nfc < M and board[nfr][nfc] == '.':
                    nf.append((nfr, nfc))
                    board[nfr][nfc] = "F"
        fire = nf
        tq, nq = q, deque()
        while tq:
            curR, curC = q.popleft()
            if curR == 0 or curR == N - 1 or curC == 0 or curC == M - 1:
                minDist = min(minDist, dist)
                continue
            for d in dirs:
                nxtR, nxtC = curR + d[0], curC + d[1]
                if 0 <= nxtR < N and 0 <= nxtC < M and board[nxtR][nxtC] == '.' and (nxtR, nxtC) not in visited:
                    nq.append((nxtR, nxtC))
                    visited.add((nxtR, nxtC))
        q = nq
        dist += 1

    print(minDist if minDist != float("inf") else "IMPOSSIBLE")
    exit(0)

def check():
    start = (-1, -1)
    fire = []
    for r in range(N):
        for c in range(M):
            if board[r][c] == "J":
                board[r][c] = '.'
                start = (r, c)
            elif board[r][c] == "F":
                fire.append((r, c))

    bfs(start, fire)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N, M = list(map(int, sys.stdin.readline().split()))
board = []
for _ in range(N):
    b = [str(x) for x in input()]
    board.append(b)
check()