import sys
sys.setrecursionlimit(10**6)

def solve(N, board, pos):
    N, board, pos = N, board, pos
    spellDirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    marbles = {1 : 0,
               2 : 0,
               3 : 0}
    for i in range(len(pos)):
        pos[i][0] -= 1

    shark = [int((N+1)/2 - 1), int((N+1)/2 - 1)]
    spiral, allSpiral = getSpiral(board, shark[0], shark[1])

    for p in pos:
        curR, curC = shark
        curSpellDirIdx, curEffect = p
        curSpellDir = spellDirs[curSpellDirIdx]
        destroyed, affected = set(), set()

        for _ in range(curEffect):
            curR += curSpellDir[0]
            curC += curSpellDir[1]
            affected.add((curR, curC))
            destroyed.add((curR, curC))

        for sR, sC, sM in spiral:
            if (sR, sC) in destroyed:
                marbles[sM] -= 1

        while len(affected) > 0:
            subtractor = 0
            newSpiral = []
            for i in range(len(spiral)):
                curIdx = i - subtractor
                sR, sC, sM = spiral[curIdx][0], spiral[curIdx][1], spiral[curIdx][2]
                if (spiral[i][0], spiral[i][1]) in affected:
                    subtractor += 1
                    marbles[spiral[i][2]] += 1
                    continue
                newSpiral.append([sR, sC, spiral[i][2]])

            affected.clear()
            mightBeRemoved = set()
            prvMarble, count = -1, 1
            for sR, sC, sM in newSpiral:
                if prvMarble != sM:
                    prvMarble = sM
                    mightBeRemoved.clear()

                mightBeRemoved.add((sR, sC))
                if len(mightBeRemoved) > 3:
                    affected = affected.union(mightBeRemoved)

            spiral = newSpiral

        updatedSpiral = []
        i = 0
        while i < len(allSpiral) - 1 and len(spiral) > 0:
            toBeRemoved, count, prvSpiralMarble = [], 1, spiral[0][2]
            lastIdx = 1
            for j in range(1, len(spiral)):
                curSpiralMarble = spiral[j][2]
                if prvSpiralMarble == curSpiralMarble:
                    count += 1
                    lastIdx = j + 1
                else:
                    break

            for k in range(lastIdx):
                spiral.pop(0)

            updatedSpiral.append([allSpiral[i][0], allSpiral[i][1], count])
            updatedSpiral.append([allSpiral[i + 1][0], allSpiral[i + 1][1], prvSpiralMarble])
            i += 2

        spiral = updatedSpiral

    return marbles[1] + marbles[2] * 2 + marbles[3] * 3

def getSpiral(board, curR, curC):
    spiral, allSpiral = [], []
    dirsForSpiral = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    curD, curLimit, count = 0, 1, 1
    board[curR][curC] = -1
    outOfBounds = False
    while True:
        d = dirsForSpiral[curD]
        for _ in range(curLimit):
            curR += d[0]
            curC += d[1]
            if (curR < 0 or curC < 0 or curR >= N or curC >= N):
                outOfBounds = True
                break

            if board[curR][curC] != 0:
                spiral.append([curR, curC, board[curR][curC]])
            allSpiral.append([curR, curC])

        if outOfBounds:
            break

        if curD == 1 or curD == 3:
            curLimit += 1

        count += 1
        curD += 1
        if curD > 3:
            curD = 0

    return spiral, allSpiral

sys.stdin = open("wizardsharkandblizzard.txt", "r")
first = list(map(int, input().split(" ")))
N, numberOfTimes = first[0], first[1]
board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))

pos = []
for _ in range(numberOfTimes):
    pos.append(list(map(int, input().split(" "))))

print(solve(N, board, pos))
