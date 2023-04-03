import sys
from collections import defaultdict
from collections import deque

V, E, P = list(map(int, input().split(" ")))
graph = defaultdict(list)
for _ in range(E):
    src, dest, cost = list(map(int, sys.stdin.readline().split(" ")))
    graph[src - 1].append((dest - 1, cost))
    graph[dest - 1].append((src - 1, cost))

def solve():
    def dijkstra():
        fromTheStart = [float("inf")] * V
        fromTheStart[0] = 0
        q = deque([(0, 0)])
        while q:
            curV, curCost = q.popleft()
            if fromTheStart[curV] < curCost:
                continue

            for neighbors in graph[curV]:
                nxtV, nxtCost = neighbors[0], neighbors[1] + curCost
                if fromTheStart[nxtV] <= nxtCost:
                    continue
                fromTheStart[nxtV] = nxtCost
                q.append((nxtV, nxtCost))

        fromP = [float("inf")] * V
        fromP[P - 1] = 0
        q = deque([(P - 1, 0)])
        while q:
            curV, curCost = q.popleft()
            if fromP[curV] < curCost:
                continue

            for neighbors in graph[curV]:
                nxtV, nxtCost = neighbors[0], neighbors[1] + curCost
                if fromP[nxtV] <= nxtCost:
                    continue
                fromP[nxtV] = nxtCost
                q.append((nxtV, nxtCost))

        if fromP[0] + fromP[-1] == fromTheStart[-1]:

            return True

        return False

    if dijkstra():
        print("SAVE HIM")
    else:
        print("GOOD BYE")

solve()