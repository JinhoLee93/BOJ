from collections import defaultdict
from collections import deque

V, E, P = list(map(int, input().split(" ")))
paths = []
for _ in range(E):
    paths.append(list(map(int, input().split(" "))))

def solve():
    graph = defaultdict(list)
    for path in paths:
        src, dest, cost = path[0] - 1, path[1] - 1, path[2]
        graph[src].append((dest, cost))
        graph[dest].append((src, cost))

    def dijkstra():
        fromTheStart = [float("inf") for _ in range(V)]
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

        fromP = [float("inf") for _ in range(V)]
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