import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

N, M = list(map(int, input().split(" ")))
board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))

def solve():
    icebergs = []
    for r in range(N):
        for c in range(M):
            if board[r][c] != 0:
                icebergs.append((board[r][c], r, c))

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    year = 1
    while icebergs:
        toBeRemoved, toBeUpdated = set(), []
        for i in range(len(icebergs)):
            curIceberg, curR, curC = icebergs[i]
            count = 0
            for d in dirs:
                nxtR, nxtC = curR + d[0], curC + d[1]
                if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= M or \
                    board[nxtR][nxtC] != 0:
                    continue
                count += 1
                if count >= curIceberg:
                    break

            if count >= curIceberg:
                toBeRemoved.add(i)
                continue

            toBeUpdated.append((i, count))

        newIcebergs = []
        for i, count in toBeUpdated:
            iceberg, r, c = icebergs[i]
            board[r][c] -= count
            newIcebergs.append((board[r][c], r, c))

        for i in toBeRemoved:
            _, r, c = icebergs[i]
            board[r][c] = 0

        icebergs = newIcebergs
        if not icebergs or len(icebergs) == 1:
            break

        bfs = deque([(icebergs[0][1], icebergs[0][2])])
        visited = set()
        while bfs:
            curR, curC = bfs.popleft()
            for d in dirs:
                nxtR, nxtC = curR + d[0], curC + d[1]
                if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= M or \
                    board[nxtR][nxtC] == 0 or (nxtR, nxtC) in visited:
                    continue
                visited.add((nxtR, nxtC))
                bfs.append((nxtR, nxtC))

        if len(visited) != len(icebergs):

            return year

        year += 1

    return 0

print(solve())