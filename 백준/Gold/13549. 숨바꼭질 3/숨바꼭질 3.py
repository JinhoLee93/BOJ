import sys
from collections import deque

N, K = list(map(int, input().split(" ")))

q = deque([(N, 0)])
timeTable = {}
while q:
    curC, curT = q.popleft()
    if curC in timeTable.keys():
        if timeTable[curC] > curT:
            timeTable[curC] = curT
        else:
            continue
    else:
        timeTable[curC] = curT

    if curC - 1 >= 0:
        q.append((curC - 1, curT + 1))

    if curC + 1 < K * 2 + 1:
        q.append((curC + 1, curT + 1))

    if curC * 2 < K * 2 + 1:
        q.append((curC * 2, curT))

print(timeTable[K])