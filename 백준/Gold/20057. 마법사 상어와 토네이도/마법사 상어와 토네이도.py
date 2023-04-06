N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().strip().split())))

def solve():
    def updateSand(curR, curC, curD):
        if curD == 0:
            candidates = [(-2, 0, 2), (-1, 0, 7), (1, 0, 7), (2, 0, 2),
                          (-1, 1, 1), (1, 1, 1), (-1, -1, 10), (1, -1, 10),
                          (0, -2, 5), (0, -1, -1)]
        elif curD == 2:
            candidates = [(-2, 0, 2), (-1, 0, 7), (1, 0, 7), (2, 0, 2),
                          (-1, 1, 10), (1, 1, 10), (-1, -1, 1), (1, -1, 1),
                          (0, 2, 5), (0, 1, -1)]
        elif curD == 1:
            candidates = [(-1, -1, 1), (-1, 1, 1), (0, -1, 7), (0, -2, 2),
                          (0, 1, 7), (0, 2, 2), (1, -1, 10), (1, 1, 10),
                          (2, 0, 5), (1, 0, -1)]
        else:
            candidates = [(-1, -1, 10), (-1, 1, 10), (0, -1, 7), (0, -2, 2),
                          (0, 1, 7), (0, 2, 2), (1, -1, 1), (1, 1, 1),
                          (-2, 0, 5), (-1, 0, -1)]
        curSand = board[curR][curC]
        outOfBounds, lump = 0, 0
        for i in range(len(candidates) - 1):
            c = candidates[i]
            cR, cC, cP = c
            uR, uC = curR + cR, curC + cC
            applied = (curSand * cP) // 100
            if uR < 0 or uC < 0 or uR >= N or uC >= N:
                outOfBounds += applied
                continue
            board[uR][uC] += applied
            lump += applied

        alpha = (curSand - (lump + outOfBounds))
        lastR, lastC, _ = candidates[-1]
        lR, lC = curR + lastR, curC + lastC
        if lR < 0 or lC < 0 or lR >= N or lC >= N:
            outOfBounds += alpha
        else:
            board[lR][lC] += alpha
        board[curR][curC] = 0

        return outOfBounds

    res = 0
    path = []
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    center = N // 2
    curR, curC, curD = center, center, 0
    adder, endMet = 1, False
    path.append((curR, curC))
    while not endMet:
        for _ in range(2):
            for a in range(adder):
                curR += dirs[curD][0]
                curC += dirs[curD][1]
                res += updateSand(curR, curC, curD)
                path.append((curR, curC))
                if (curR, curC) == (0, 0):
                    endMet = True
                    break
            if endMet:
                break
            curD += 1
            if curD == 4:
                curD = 0
        adder += 1
    print(res)

solve()