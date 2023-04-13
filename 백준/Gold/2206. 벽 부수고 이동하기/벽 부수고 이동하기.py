from collections import deque

def bfs():
    q = deque([(0, 0, 1, False)])
    visited = set()
    visited.add((0, 0, False))
    dist = float("inf")
    while q:
        curR, curC, curD, haveBrokenWall = q.popleft()
        if (curR, curC) == goal:
            dist = min(dist, curD)
            continue
        for d in dirs:
            nxtR, nxtC = curR + d[0], curC + d[1]
            if 0 <= nxtR < N and 0 <= nxtC < M and (nxtR, nxtC, haveBrokenWall) not in visited:
                if board[nxtR][nxtC] == 1:
                    if not haveBrokenWall:
                        q.append((nxtR, nxtC, curD + 1, True))
                else:
                    q.append((nxtR, nxtC, curD + 1, haveBrokenWall))
                visited.add((nxtR, nxtC, haveBrokenWall))

    return dist if dist != float("inf") else -1

N, M = map(int, input().split())
board = []
for _ in range(N):
    b = [int(x) for x in input()]
    board.append(b)
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
goal = (N - 1, M - 1)
print(bfs())