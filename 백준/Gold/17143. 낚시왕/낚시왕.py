def solve(r, c, m, sharks):
    R, C, M = r, c, m
    fisher, caught = -1, []
    board = {}

    for s in sharks:
        s[0] -= 1
        s[1] -= 1
        s[3] -= 1
        sharkMeta = (s[2], s[3], s[4])
        board[(s[0], s[1])] = sharkMeta

    while fisher < C - 1:
        fisher += 1
        for r in range(R):
            if (r, fisher) in board.keys():
                caught.append(board[(r, fisher)])
                board.pop((r, fisher))
                break

        tempBoard = {}

        for key in board.keys():
            curR, curC = key[0], key[1]
            s = board[key]
            curSpeed, curD = s[0], s[1]
            curSize = s[2]

            nextR, nextC = curR, curC
            if curD == 0: # Up
                nextR = curR - curSpeed
            elif curD == 1: # Down
                nextR = curR + curSpeed
            elif curD == 2: # Right
                nextC = curC + curSpeed
            else: # Left
                nextC = curC - curSpeed

            modR, modC = (R - 1) * 2, (C - 1) * 2
            nextD = curD
            if nextR < 0:
                afterMod = nextR % modR
                if afterMod >= (R - 1):
                    posMod = afterMod % (R - 1)
                    nextR = R - 1 - posMod
                    nextD = 1
                else:
                    nextR = afterMod

            elif nextR > R - 1:
                afterMod = nextR % modR
                if afterMod >= (R - 1):
                    posMod = afterMod % (R - 1)
                    nextR = R - 1 - posMod
                    nextD = 0
                else:
                    nextR = afterMod

            elif nextC < 0:
                afterMod = nextC % modC
                if afterMod >= (C - 1):
                    posMod = afterMod % (C - 1)
                    nextC = C - 1 - posMod
                    nextD = 2
                else:
                    nextC = afterMod

            elif nextC > C - 1:
                afterMod = nextC % modC
                if afterMod >= (C - 1):
                    posMod = afterMod % (C - 1)
                    nextC = C - 1 - posMod
                    nextD = 3
                else:
                    nextC = afterMod

            nextKey = (nextR, nextC)
            nextVal = (curSpeed, nextD, curSize)
            if nextKey in tempBoard:
                if tempBoard[nextKey][2] < curSize:
                    tempBoard[nextKey] = nextVal
            else:
                tempBoard[nextKey] = nextVal

        board = tempBoard

    res = 0
    for c in caught:
        res += c[2]

    return res

R, C, M = tuple(map(int, input().split(" ")))
sharks = []
for m in range(M):
    sharks.append(list(map(int, input().split(" "))))
print(solve(R, C, M, sharks))