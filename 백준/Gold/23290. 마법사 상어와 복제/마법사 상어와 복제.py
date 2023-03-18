def solve(attempt, fish, shark):
    shark = shark
    res = 0
    board = {}
    smellBoard = {}
    fishDirs = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    sharkDirs = [1, 2, 3, 4]
    sharkDirsInCoor = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    combs = []
    def backtrack(i, temp):
        if len(temp) == 3:
            combs.append(temp.copy())

            return

        for j in range(4):
            temp.append(sharkDirs[j])
            backtrack(j + 1, temp)
            temp.pop()

    backtrack(0, [])
    combs.sort(key=lambda x:int(str(x[0]) + str(x[1]) + str(x[2])))

    for r in range(1, 5):
        for c in range(1, 5):
            board[(r, c)] = [] # fishDirs
            smellBoard[(r, c)] = [] # Turns in which smell was created

    for f in fish:
        f[2] -= 1
        board[(f[0], f[1])].append(f[2])

    for a in range(attempt):
        nextBoard = {}
        for r in range(1, 5):
            for c in range(1, 5):
                nextBoard[(r, c)] = []

        # Fish moves
        for key in board.keys():
            fishInCell = board[key]
            for f in fishInCell:
                curX, curY, curD = key[0], key[1], f
                stayStill = False
                while curX + fishDirs[curD][0] < 1 or curY + fishDirs[curD][1] < 1 or \
                    curX + fishDirs[curD][0] > 4 or curY + fishDirs[curD][1] > 4 or \
                    (curX + fishDirs[curD][0], curY + fishDirs[curD][1]) == shark or \
                    len(smellBoard[(curX + fishDirs[curD][0], curY + fishDirs[curD][1])]) > 0:
                    curD = turn45Counterclockwise(curD)
                    if curD == f:
                        stayStill = True
                        break

                if not stayStill:
                    curX += fishDirs[curD][0]
                    curY += fishDirs[curD][1]

                nextFish = (curX, curY)
                nextBoard[nextFish].append(curD)

        # Shark moves
        cellsSharkCanGo = []
        maximumFish = float("-inf")
        for sd in combs:
            nextShark = shark
            curFish = 0
            failed = False
            visited = set()
            for d in sd:
                curD = d - 1
                nextSharkX, nextSharkY = nextShark[0] + sharkDirsInCoor[curD][0], nextShark[1] + sharkDirsInCoor[curD][1]
                if nextSharkX < 1 or nextSharkY < 1 or nextSharkX > 4 or nextSharkY > 4:
                    failed = True
                    break

                nextShark = (nextSharkX, nextSharkY)
                if nextShark not in visited:
                    curFish += len(nextBoard[nextShark])
                visited.add(nextShark)

            if not failed:
                if maximumFish < curFish:
                    maximumFish = curFish
                    cellsSharkCanGo = sd

        for d in cellsSharkCanGo:
            curD = d - 1
            curSharkX, curSharkY = shark
            nextSharkX = curSharkX + sharkDirsInCoor[curD][0]
            nextSharkY = curSharkY + sharkDirsInCoor[curD][1]
            shark = (nextSharkX, nextSharkY)
            if len(nextBoard[shark]) > 0:
                smellBoard[shark].append(a)
                nextBoard[shark] = []

        # Smells go away
        for key in smellBoard.keys():
            toStay = []
            if len(smellBoard[key]) > 0:
                for smell in smellBoard[key]:
                    if a - smell < 2:
                        toStay.append(smell)
            smellBoard[key] = toStay

        # Copy the previous board
        for key in board.keys():
            board[key] += nextBoard[key]

    for key in board.keys():
        res += len(board[key])

    return res

def turn45Counterclockwise(curD):

    return 7 if curD < 0 else curD - 1

numberOfFish, attempt = list(map(int, input().split(" ")))
fish = [] # [fx, fy, d]
for _ in range(numberOfFish):
    fish.append(list(map(int, input().split(" "))))

shark = tuple(map(int, input().split(" ")))
print(solve(attempt, fish, shark))