N, M = map(int, input().split())
T = list(map(int, input().split()))
parties = []
for _ in range(M):
    parties.append(list(map(int, input().split())))

pplWhoKnow = set()
for t in range(1, T[0] + 1):
    pplWhoKnow.add(T[t])

graph = {}
for i in range(1, N + 1):
    graph[i] = []

for party in parties:
    for i in range(1, len(party)):
        for j in range(1, len(party)):
            if i == j:
                continue
            graph[party[i]].append(party[j])


def dfs(person):
    if person in visited:

        return

    visited.add(person)
    for nei in graph[person]:
        dfs(nei)

for i in range(1, N + 1):
    if i in pplWhoKnow:
        visited = set()
        dfs(i)
        pplWhoKnow = pplWhoKnow.union(visited)

res = 0
for party in parties:
    know = False
    for p in range(1, len(party)):
        person = party[p]
        if person in pplWhoKnow:
            know = True
            break
    if not know:
        res += 1

print(res)
