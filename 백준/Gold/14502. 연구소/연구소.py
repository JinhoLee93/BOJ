from collections import deque

def backtrack(i, temp):
    if len(temp) == 3:
        combs.append(temp.copy())

        return

    if i < len(empty):
        temp.append(empty[i])
        backtrack(i + 1, temp)
        temp.pop()
        backtrack(i + 1, temp)
def bfs(c, v, b, n):
    for cr, cc in c:
        b[cr][cc] = 1

    q = deque(v)
    while q:
        curR, curC = q.popleft()
        for d in dirs:
            nxtR, nxtC = curR + d[0], curC + d[1]
            if 0 <= nxtR < N and 0 <= nxtC < M and b[nxtR][nxtC] == 0:
                b[nxtR][nxtC] = 2
                q.append((nxtR, nxtC))
                n -= 1

    return n

N, M = map(int, input().strip().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().strip().split())))
dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
empty, virus = [], []
for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            empty.append((r, c))
        elif board[r][c] == 2:
            virus.append((r, c))
combs = []
backtrack(0, [])
res, numOfEmptyCells = 0, len(empty) - 3
for c in combs:
    b = [[0] * M for _ in range(N)]
    for cr in range(N):
        for cc in range(M):
            b[cr][cc] = board[cr][cc]
    res = max(res, bfs(c, virus, b, numOfEmptyCells))

print(res)