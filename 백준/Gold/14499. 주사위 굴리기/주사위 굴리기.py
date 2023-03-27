import sys
from collections import deque

N, M, diceR, diceC, K = list(map(int, input().split(" ")))
board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))
dirsToGo = list(map(int, input().split(" ")))
for i in range(len(dirsToGo)):
    dirsToGo[i] -= 1

def solve():
    horizontal = [0, 0]
    parallel = deque([0, 0, 0, 0])
    curDice = (diceR, diceC)
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    res = []
    for toGo in dirsToGo:
        curR, curC = curDice
        curDir = dirs[toGo]

        nxtR, nxtC = curR + curDir[0], curC + curDir[1]
        if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= M:
            continue

        if toGo == 0:
            horizontal[0], parallel[1] = parallel[1], horizontal[0]
            horizontal[1], parallel[3] = parallel[3], horizontal[1]
            horizontal.reverse()
        elif toGo == 1:
            horizontal[0], parallel[3] = parallel[3], horizontal[0]
            horizontal[1], parallel[1] = parallel[1], horizontal[1]
            horizontal.reverse()
        elif toGo == 2:
            bottom = parallel.popleft()
            parallel.append(bottom)
        else:
            bottom = parallel.pop()
            parallel.appendleft(bottom)

        if board[nxtR][nxtC] == 0:
            board[nxtR][nxtC] = parallel[3]
        else:
            parallel[3] = board[nxtR][nxtC]
            board[nxtR][nxtC] = 0

        curDice = (nxtR, nxtC)
        res.append(parallel[1])

    return res

res = solve()
for r in res:
    print(r)