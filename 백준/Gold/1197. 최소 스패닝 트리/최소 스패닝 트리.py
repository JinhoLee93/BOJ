from collections import defaultdict
import heapq

V, E = list(map(int, input().strip().split()))
paths = []
for _ in range(E):
    paths.append(list(map(int, input().strip().split())))

def solve():
    graph = defaultdict(list)

    for p in paths:
        s, d, c = p
        graph[s - 1].append((c, d - 1))
        graph[d - 1].append((c, s - 1))

    for key in graph:
        graph[key].sort(key=lambda x:x[0])

    res = 0
    q = [[0, 0]]
    visited = set()
    while q:
        cost, to = heapq.heappop(q)
        if to not in visited:
            visited.add(to)
            res += cost
            if len(visited) == V:
                print(res)
                exit(0)
            for n in graph[to]:
                if n[1] not in visited:
                    heapq.heappush(q, n)
solve()