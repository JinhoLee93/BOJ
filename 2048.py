import sys

def solve(N, fromInput):
    R, C = N, N
    board = fromInput
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    maxVal = -1
    q = [(board, 0)]
    while q:
        cur = q.pop(0)
        curBoard, iter = cur[0], cur[1]
        if iter == 5:
            for r in range(R):
                for c in range(C):
                    maxVal = max(maxVal, curBoard[r][c])

        elif iter > 5:
            break

        for d in dir:
            nextBoard = [row[:] for row in curBoard]
            mergedCells = set()
            if d == [-1, 0]: # up
                for c in range(0, C):
                    for r in range(1, R):
                        if nextBoard[r][c] == 0:
                            continue
                        if nextBoard[r - 1][c] == 0:
                            lastEmptyRow = -1
                            for br in range(r - 1, -1, -1):
                                if nextBoard[br][c] == 0:
                                    lastEmptyRow = br
                            if lastEmptyRow == 0:
                                nextBoard[lastEmptyRow][c] = nextBoard[r][c]
                            else:
                                if nextBoard[lastEmptyRow - 1][c] == nextBoard[r][c] and (lastEmptyRow - 1, c) not in mergedCells:
                                    mergedCells.add((lastEmptyRow - 1, c))
                                    nextBoard[lastEmptyRow - 1][c] += nextBoard[r][c]
                                else:
                                    nextBoard[lastEmptyRow][c] = nextBoard[r][c]
                            nextBoard[r][c] = 0
                        else:
                            if nextBoard[r - 1][c] == nextBoard[r][c] and (r - 1, c) not in mergedCells:
                                mergedCells.add((r - 1, c))
                                nextBoard[r - 1][c] += nextBoard[r][c]
                                nextBoard[r][c] = 0

            elif d == [1, 0]: # down
                for c in range(0, C):
                    for r in range(R - 2, -1, -1):
                        if nextBoard[r][c] == 0:
                            continue
                        if nextBoard[r + 1][c] == 0:
                            lastEmptyRow = -1
                            for br in range(r + 1, R):
                                if nextBoard[br][c] == 0:
                                    lastEmptyRow = br
                            if lastEmptyRow == R - 1:
                                nextBoard[lastEmptyRow][c] = nextBoard[r][c]
                            else:
                                if nextBoard[lastEmptyRow + 1][c] == nextBoard[r][c] and (lastEmptyRow + 1, c) not in mergedCells:
                                    mergedCells.add((lastEmptyRow + 1, c))
                                    nextBoard[lastEmptyRow + 1][c] += nextBoard[r][c]
                                else:
                                    nextBoard[lastEmptyRow][c] = nextBoard[r][c]
                            nextBoard[r][c] = 0
                        else:
                            if nextBoard[r + 1][c] == nextBoard[r][c] and (r + 1, c) not in mergedCells:
                                mergedCells.add((r + 1, c))
                                nextBoard[r + 1][c] += nextBoard[r][c]
                                nextBoard[r][c] = 0

            elif d == [0, 1]: # right
                for r in range(0, R):
                    for c in range(C - 2, -1, -1):
                        if nextBoard[r][c] == 0:
                            continue
                        if nextBoard[r][c + 1] == 0:
                            lastEmptyCol = -1
                            for bc in range(c + 1, C):
                                if nextBoard[r][bc] == 0:
                                    lastEmptyCol = bc
                            if lastEmptyCol == C - 1:
                                nextBoard[r][lastEmptyCol] = nextBoard[r][c]
                            else:
                                if nextBoard[r][lastEmptyCol + 1] == nextBoard[r][c] and (r, lastEmptyCol + 1) not in mergedCells:
                                    mergedCells.add((r, lastEmptyCol + 1))
                                    nextBoard[r][lastEmptyCol + 1] += nextBoard[r][c]
                                else:
                                    nextBoard[r][lastEmptyCol] = nextBoard[r][c]
                            nextBoard[r][c] = 0
                        else:
                            if nextBoard[r][c + 1] == nextBoard[r][c] and (r, c + 1) not in mergedCells:
                                mergedCells.add((r, c + 1))
                                nextBoard[r][c + 1] += nextBoard[r][c]
                                nextBoard[r][c] = 0

            elif d == [0, -1]: # left
                for r in range(0, R):
                    for c in range(1, C):
                        if nextBoard[r][c] == 0:
                            continue
                        if nextBoard[r][c - 1] == 0:
                            lastEmptyCol = -1
                            for bc in range(c - 1, -1, -1):
                                if nextBoard[r][bc] == 0:
                                    lastEmptyCol = bc
                            if lastEmptyCol == 0:
                                nextBoard[r][lastEmptyCol] = nextBoard[r][c]
                            else:
                                if nextBoard[r][lastEmptyCol - 1] == nextBoard[r][c] and (r, lastEmptyCol - 1) not in mergedCells:
                                    mergedCells.add((r, lastEmptyCol - 1))
                                    nextBoard[r][lastEmptyCol - 1] += nextBoard[r][c]
                                else:
                                    nextBoard[r][lastEmptyCol] = nextBoard[r][c]
                            nextBoard[r][c] = 0
                        else:
                            if nextBoard[r][c - 1] == nextBoard[r][c] and (r, c - 1) not in mergedCells:
                                mergedCells.add((r, c - 1))
                                nextBoard[r][c - 1] += nextBoard[r][c]
                                nextBoard[r][c] = 0

            q.append((nextBoard, iter + 1))

    return maxVal

# sys.stdin = open("2048.txt", "r")
N = int(input())
fromInput = []
for _ in range(0, N):
    fromInput.append(list(map(int, input().split(" "))))
print(solve(N, fromInput))
