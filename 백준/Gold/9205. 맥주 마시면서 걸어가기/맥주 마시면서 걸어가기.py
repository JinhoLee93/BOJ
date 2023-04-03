from collections import deque

T = int(input())

def distance(x1, x2, y1, y2):

    return abs(x2 - x1) + abs(y2 - y1)

def bfs(beer, home, stores, festival):
    stores.append(festival)
    q = deque([(home[0], home[1], beer)])
    visited = set()
    while q:
        curR, curC, beerLeft = q.popleft()
        for i, (nxtR, nxtC) in enumerate(stores):
            if i in visited:
                continue
            dtos = distance(curR, nxtR, curC, nxtC)
            if dtos > beerLeft:
                continue
            else:
                if (nxtR, nxtC) == festival:

                    return "happy"
                visited.add(i)
                q.append((nxtR, nxtC, 20 * 50))

    return "sad"

for _ in range(T):
    beer = 20 * 50 # It cannot get bigger than 20
    N = int(input())
    home = list(map(int, input().split(" ")))
    stores = []
    for _ in range(N):
        stores.append(list(map(int, input().split(" "))))
    festival = tuple(map(int, input().split(" ")))

    print(bfs(beer, home, stores, festival))