N, M, K = list(map(int, input().split(" ")))
board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))

curSharkDirs = list(map(int, input().split(" ")))
for i in range(len(curSharkDirs)):
    curSharkDirs[i] -= 1

sharks = [[[] for _ in range(4)] for _ in range(M)]
for i in range(M):
    for j in range(4):
        sharks[i][j] = list(map(int, input().split(" ")))
        for k in range(len(sharks[i][j])):
            sharks[i][j][k] -= 1

# Shark's directions = 0 = UP, 1 = DOWN, 2 = LEFT, 3 = RIGHT
def solve(board, sharks, curSharkDirs, k):
    numOfSharks = len(curSharkDirs)
    N = len(board)
    smellBoard = [[[] for _ in range(N)] for _ in range(N)]
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    sharksPos = []
    for r in range(N):
        for c in range(N):
            if board[r][c] > 0:
                sharksPos.append((r, c, board[r][c]))
                smellBoard[r][c] = [board[r][c], k]

    for num in range(1000):
        newBoard = [[0 for _ in range(N)] for _ in range(N)]

        # Getting the next cell for the sharks
        sharksPos.sort(key=lambda x:x[2])
        toBeRemoved = set()
        for i in range(len(sharksPos)):
            sd = curSharkDirs[i]
            if sd == -1:
                continue
            curSharkR, curSharkC, curSharkNum = sharksPos[i][0], sharksPos[i][1], sharksPos[i][2]
            nxtSharkDirCandidates = sharks[i][sd]
            possibleNextCell = []
            possibleNextDir = -1
            for d in nxtSharkDirCandidates:
                moveTo = dirs[d]
                nxtSharkR, nxtSharkC = curSharkR + moveTo[0], curSharkC + moveTo[1]
                if nxtSharkR >= N or nxtSharkC >= N or nxtSharkR < 0 or nxtSharkC < 0:
                    continue

                if not smellBoard[nxtSharkR][nxtSharkC]:
                    possibleNextCell = [nxtSharkR, nxtSharkC]
                    possibleNextDir = d
                    break

                if smellBoard[nxtSharkR][nxtSharkC][0] == curSharkNum and not possibleNextCell:
                    possibleNextCell = [nxtSharkR, nxtSharkC]
                    possibleNextDir = d

            if newBoard[possibleNextCell[0]][possibleNextCell[1]] > 0:
                sharksPos[i] = (-1, -1, curSharkNum)
                curSharkDirs[i] = -1
                numOfSharks -= 1
                continue

            newBoard[possibleNextCell[0]][possibleNextCell[1]] = curSharkNum
            sharksPos[i] = (possibleNextCell[0], possibleNextCell[1], curSharkNum)
            curSharkDirs[i] = possibleNextDir

        addSmell = []
        for r in range(N):
            for c in range(N):
                if newBoard[r][c] > 0:
                    addSmell.append((r, c, newBoard[r][c]))

        for r in range(N):
            for c in range(N):
                if smellBoard[r][c]:
                    smellBoard[r][c][1] -= 1
                    if smellBoard[r][c][1] == 0:
                        smellBoard[r][c] = []

        for a in addSmell:
            smellBoard[a[0]][a[1]] = [newBoard[a[0]][a[1]], k]

        board = newBoard

        if numOfSharks == 1:

            return num + 1

    return -1

print(solve(board, sharks, curSharkDirs, K))