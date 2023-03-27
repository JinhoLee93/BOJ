import sys
import copy
from collections import deque
from collections import defaultdict
sys.setrecursionlimit(10**6)

N, M, K = list(map(int, input().split(" ")))
board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))

def solve():
    res = 0
    curDiceCoor = (0, 0)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    curDir = 0
    horizontal = [4, 3]
    parallel = deque([2, 1, 5, 6]) # parallel[3] = bottom
    first = True

    for _ in range(K):
        curR, curC = curDiceCoor
        if not first:
            if parallel[3] > board[curR][curC]:
                curDir = (curDir + 1) % 4
            elif parallel[3] < board[curR][curC]:
                curDir -= 1
                if curDir < 0:
                    curDir = 3
        else:
            first = False

        nxtR, nxtC = curR + dirs[curDir][0], curC + dirs[curDir][1]
        if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= M:
            if curDir == 0:
                curDir = 2
            elif curDir == 2:
                curDir = 0
            elif curDir == 1:
                curDir = 3
            else:
                curDir = 1
            nxtR, nxtC = curR + dirs[curDir][0], curC + dirs[curDir][1]

        if curDir == 0:
            horizontal[0], parallel[1] = parallel[1], horizontal[0]
            horizontal[1], parallel[3] = parallel[3], horizontal[1]
            horizontal.reverse()
        elif curDir == 1:
            bottom = parallel.pop()
            parallel.appendleft(bottom)
        elif curDir == 2:
            horizontal[0], parallel[3] = parallel[3], horizontal[0]
            horizontal[1], parallel[1] = parallel[1], horizontal[1]
            horizontal.reverse()
        else:
            bottom = parallel.popleft()
            parallel.append(bottom)
        curDiceCoor = (nxtR, nxtC)
        curBoardNum = board[nxtR][nxtC]
        possibleCells = 1
        q = deque([curDiceCoor])
        visited = set()
        visited.add(curDiceCoor)
        while q:
            cr, cc = q.popleft()
            for d in dirs:
                nr, nc = cr + d[0], cc + d[1]
                if nr < 0 or nc < 0 or nr >= N or nc >= M or (nr, nc) in visited:
                    continue

                visited.add((nr, nc))
                if board[nr][nc] == curBoardNum:
                    q.append((nr, nc))
                    possibleCells += 1

        res += possibleCells * curBoardNum

    return res

print(solve())