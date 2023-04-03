import sys
import heapq
from collections import defaultdict

V, E = list(map(int, input().split(" ")))
S = int(input()) - 1
distMap = [float("inf")] * V
paths = defaultdict(list)
for _ in range(E):
    src, dest, cost = list(map(int, sys.stdin.readline().split(" ")))
    paths[src - 1].append((dest - 1, cost))

def solve():
    distMap[S] = 0
    q = []
    heapq.heappush(q, (0, S))
    while q:
        curCost, curV = heapq.heappop(q)
        if distMap[curV] < curCost:
            continue

        for nei in paths[curV]:
            nxtV, nxtCost = nei[0], nei[1] + curCost
            if distMap[nxtV] > nxtCost:
                distMap[nxtV] = nxtCost
                heapq.heappush(q, (nxtCost, nxtV))

    for d in distMap:
        if d == float("inf"):
            print("INF")
        else:
            print(d)

solve()