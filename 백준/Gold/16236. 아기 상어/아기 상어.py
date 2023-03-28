import sys
from collections import deque

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))

def solve():
    fish = {}
    curShark, curSharkSize, ate = [], 2, 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 9:
                curShark = [r, c]
                board[r][c] = 0
            elif board[r][c] > 0:
                fish[(r, c)] = board[r][c]

    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    time = 0
    while fish:
        curSharkR, curSharkC = curShark[0], curShark[1]
        q = deque([(curSharkR, curSharkC)])
        toBeEaten, visited = [], set()
        visited.add((curSharkR, curSharkC))
        dist = 1
        while q:
            nxtQ = []
            temp = deque(q)
            while temp:
                cur = temp.popleft()
                curR, curC = cur[0], cur[1]
                for d in dirs:
                    nxtR, nxtC = curR + d[0], curC + d[1]
                    if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= N or \
                        board[nxtR][nxtC] > curSharkSize or \
                        (nxtR, nxtC) in visited:
                        continue
                    visited.add((nxtR, nxtC))
                    if board[nxtR][nxtC] > 0 and board[nxtR][nxtC] < curSharkSize:
                        toBeEaten.append((nxtR, nxtC, dist))
                    nxtQ.append((nxtR, nxtC))
            if toBeEaten:
                break
            q = nxtQ
            dist += 1
        if not toBeEaten:

            return time
        toBeEaten.sort(key=lambda x:(x[0], x[1]))
        willBeEaten = toBeEaten[0]
        board[willBeEaten[0]][willBeEaten[1]] = 0
        fish.pop((willBeEaten[0], willBeEaten[1]))
        curShark = (willBeEaten[0], willBeEaten[1])
        ate += 1
        if ate == curSharkSize:
            curSharkSize += 1
            ate = 0
        time += willBeEaten[2]

    return time

print(solve())