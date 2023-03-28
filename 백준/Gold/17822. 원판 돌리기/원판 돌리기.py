import sys
from collections import deque

N, M, T = list(map(int, input().split(" ")))
board = []
for _ in range(N):
    board.append(deque(list(map(int, input().split(" ")))))

rotations = deque([]) # x, d: if 0, clockwise, if 1, counterclockwise, k: how many blocks you will be moving
for _ in range(T):
    rotations.append(deque(list(map(int, input().split(" ")))))

def solve():
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while rotations:
        cur = rotations.popleft()
        curX, curD, curK = cur[0], cur[1], cur[2] % M
        disks = []
        for i in range(N):
            if (i + 1) % curX == 0:
                disks.append(i)

        for i in disks:
            for j in range(curK):
                if curD == 0: # clockwise
                    first = board[i].pop()
                    board[i].appendleft(first)
                else: # counterclockwise
                    last = board[i].popleft()
                    board[i].append(last)

        nearAndTheSame = set()
        for r in range(N):
            for c in range(M):
                curVal = board[r][c]
                if curVal == float("-inf"):
                    continue

                curNearAndTheSame = set()
                for d in dirs:
                    nxtR, nxtC = r + d[0], c + d[1]
                    if nxtR < 0 or nxtR >= N:
                        continue

                    if nxtC < 0:
                        nxtC = M - 1
                    elif nxtC >= M:
                        nxtC = 0

                    if board[nxtR][nxtC] == float("-inf"):
                        continue

                    if board[nxtR][nxtC] == curVal:
                        curNearAndTheSame.add((nxtR, nxtC))

                if curNearAndTheSame:
                    curNearAndTheSame.add((r, c))
                nearAndTheSame = nearAndTheSame.union(curNearAndTheSame)

        for r, c in nearAndTheSame:
            board[r][c] = float("-inf")

        if not nearAndTheSame:
            sumOfElem, numOfElem, cellsWithElem = 0, 0, set()
            for r in range(N):
                for c in range(M):
                    if board[r][c] == float("-inf"):
                        continue
                    sumOfElem += board[r][c]
                    numOfElem += 1
                    cellsWithElem.add((r, c))

            if numOfElem == 0:
                break
            average = float(sumOfElem / numOfElem) # Remember this condition
            for cr, cc in cellsWithElem:
                if board[cr][cc] > average:
                    board[cr][cc] -= 1
                elif board[cr][cc] < average:
                    board[cr][cc] += 1

    res = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == float("-inf"):
                continue
            res += board[r][c]

    return res

print(solve())