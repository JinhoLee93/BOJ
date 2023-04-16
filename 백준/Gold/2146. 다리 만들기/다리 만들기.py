import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

def dfs(r, c, temp):
    if 0 <= r < N and 0 <= c < N and board[r][c] == 1 and \
        (r, c) not in visited:
        temp.add((r, c))
        visited.add((r, c))

        dfs(r + 1, c, temp)
        dfs(r - 1, c, temp)
        dfs(r, c + 1, temp)
        dfs(r, c - 1, temp)

def bfs(curIsland):
    q = deque(curIsland)
    cur = set(curIsland)
    dist = 0
    v = set()
    while q:
        tempQ, nxtQ = q, deque()
        while tempQ:
            cr, cc = tempQ.popleft()
            for d in dirs:
                nr, nc = cr + d[0], cc + d[1]
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in cur and (nr, nc) not in v:
                    if board[nr][nc] == 1:
                        return dist
                    v.add((nr, nc))
                    nxtQ.append((nr, nc))
        dist += 1
        q = nxtQ

N = int(input())
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited, islands = set(), []
for r in range(N):
    for c in range(N):
        if board[r][c] == 1 and (r, c) not in visited:
            island = set()
            dfs(r, c, island)
            islands.append(list(island))

res = float("inf")
for island in islands:
    res = min(res, bfs(island))
print(res)