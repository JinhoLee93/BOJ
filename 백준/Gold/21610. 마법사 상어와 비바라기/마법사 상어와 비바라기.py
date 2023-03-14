def solve(N, board, pos):
    N, board, pos = N, board, pos
    for p in pos:
        p[0] -= 1

    clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
    dirs = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    diag = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

    for p in pos:
        dirIdx, distanceToMove = p[0], p[1]
        d = dirs[dirIdx]

        curClouds = set()
        for cloud in clouds:
            curR, curC = cloud[0], cloud[1]
            curR = (curR + d[0] * distanceToMove) % N
            curC = (curC + d[1] * distanceToMove) % N

            board[curR][curC] += 1
            curClouds.add((curR, curC))

        for cloud in curClouds:
            curR, curC = cloud[0], cloud[1]
            adder = 0
            for di in diag:
                checkR, checkC = curR + di[0], curC + di[1]
                if checkR >= N or checkC >= N or checkR < 0 or checkC < 0:
                    continue
                if board[checkR][checkC] > 0:
                    adder += 1
            board[curR][curC] += adder

        nextClouds = []
        for r in range(N):
            for c in range(N):
                if board[r][c] > 1 and (r, c) not in curClouds:
                    nextClouds.append((r, c))
                    board[r][c] -= 2

        clouds = nextClouds

    res = 0
    for r in range(N):
        for c in range(N):
            res += board[r][c]

    return res

N, M = list(map(int, input().split(" ")))
board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))

pos = []
for _ in range(M):
    pos.append(list(map(int, input().split(" "))))

print(solve(N, board, pos))