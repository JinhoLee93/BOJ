N, M, fuel = list(map(int, input().split(" ")))
board = []

for _ in range(N):
    board.append(list(map(int, input().split(" "))))

start = list(map(int, input().split(" ")))
start[0] -= 1
start[1] -= 1

customers = []
for _ in range(M):
    customers.append(list(map(int, input().split(" "))))

for i in range(len(customers)):
    customers[i][0] -= 1
    customers[i][1] -= 1
    customers[i][2] -= 1
    customers[i][3] -= 1

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def findCustomer(start):
    distMap, minDist = [], float("inf")
    q = [(start, 0)]
    visited = set()
    while q:
        cur = q.pop(0)
        curR, curC, curD = cur[0][0], cur[0][1], cur[1]
        if fuel < curD or minDist < curD:

            return distMap

        elif (curR, curC) in departureSet:
            minDist = curD
            distMap.append(((curR, curC), departureSet[(curR, curC)], curD))
            continue

        if (curR, curC) in visited:
            continue

        for d in dirs:
            nxtR, nxtC = curR + d[0], curC + d[1]
            if nxtR >= N or nxtC >= N or nxtR < 0 or nxtC < 0 or \
                board[nxtR][nxtC] == 1 or (nxtR, nxtC) in visited:
                continue

            visited.add((curR, curC))
            q.append(((nxtR, nxtC), curD + 1))

    return distMap

def bfs(start, dest):
    q = [(start, 0)]
    visited = set()
    while q:
        cur = q.pop(0)
        curR, curC, curDist = cur[0][0], cur[0][1], cur[1]
        if fuel < curDist:

            return -1

        elif (curR, curC) == dest:

            return curDist

        if (curR, curC) in visited:
            continue

        for d in dirs:
            nxtR, nxtC = curR + d[0], curC + d[1]
            if nxtR >= N or nxtC >= N or nxtR < 0 or nxtC < 0 or \
                board[nxtR][nxtC] == 1 or (nxtR, nxtC) in visited:
                continue

            visited.add((curR, curC))
            q.append(((nxtR, nxtC), curDist + 1))

    return -1

while customers:
    departureSet = {}
    for i, c in enumerate(customers):
        departureSet[(c[0], c[1])] = i

    rowCandidates = findCustomer(start)

    if not rowCandidates:
        print(-1)
        exit(0)

    rowCandidates.sort(key=lambda x:x[0])

    colCandidates = []
    lowestRow = N
    for (curR, curC), i, d in rowCandidates:
        if curR < lowestRow:
            lowestRow = curR
        elif curR > lowestRow:
            break
        colCandidates.append((curC, i, d))
    colCandidates.sort(key=lambda x:x[0])

    curCustomers = customers.pop(colCandidates[0][1])
    fuel -= colCandidates[0][2]
    if fuel <= 0:
        print(-1)
        exit(0)

    start = (curCustomers[0], curCustomers[1])
    dest = (curCustomers[2], curCustomers[3])

    successful = bfs(start, dest)
    if successful == -1:
        print(-1)
        exit(0)
    else:
        fuel -= successful
        fuel += successful * 2

    start = dest

print(fuel)