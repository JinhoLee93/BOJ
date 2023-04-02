N, M = list(map(int, input().split(" ")))
board = []
roomba = list(map(int, input().split(" ")))
for _ in range(N):
    board.append(list(map(int, input().split(" "))))

def solve(roomba):
    res = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while True:
        curR, curC, d = roomba
        if board[curR][curC] == 0:
            res += 1
        board[curR][curC] = -1
        dir = d
        nowhereToClean = True
        for _ in range(4):
            dir -= 1
            if dir < 0:
                dir = 3
            curDir = dirs[dir]
            nxtR, nxtC = curR + curDir[0], curC + curDir[1]
            if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= M or \
                board[nxtR][nxtC] != 0:
                continue
            nowhereToClean = False
            roomba = [nxtR, nxtC, dir]
            break

        if nowhereToClean:
            curDir = [-1 * dirs[dir][0], -1 * dirs[dir][1]]
            nxtR, nxtC = curR + curDir[0], curC + curDir[1]
            if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= M or \
                board[nxtR][nxtC] == 1:
                print(res)
                break
            roomba = [nxtR, nxtC, dir]

solve(roomba)
