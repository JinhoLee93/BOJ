N = int(input())
blocks = []
for _ in range(N):
    blocks.append(list(map(int, input().split(" "))))

def solve():
    res = 0
    blueBoard = [[0 for _ in range(6)] for _ in range(4)]
    greenBoard = [[0 for _ in range(4)] for _ in range(6)]

    # Place a block in the red board and the block will move
    # row-wise to the blue board and
    # col-wise to the green board.
    for block in blocks:
        t, r, c = block
        # Check the blue block
        if t == 1:
            lastCol = -1
            for blueC in range(len(blueBoard[0])):
                if blueBoard[r][blueC] == 0:
                    lastCol = blueC
                else:
                    break
            blueBoard[r][lastCol] = 1

        elif t == 2:
            lastCol = -1
            for blueC in range(1, len(blueBoard[0])):
                if blueBoard[r][blueC] == 0 and blueBoard[r][blueC - 1] == 0:
                    lastCol = blueC
                else:
                    break
            blueBoard[r][lastCol] = 1
            blueBoard[r][lastCol - 1] = 1

        elif t == 3:
            lastCol = -1
            for blueC in range(len(blueBoard[0])):
                if blueBoard[r][blueC] == 0 and blueBoard[r + 1][blueC] == 0:
                    lastCol = blueC
                else:
                    break
            blueBoard[r][lastCol] = 1
            blueBoard[r + 1][lastCol] = 1

        toBeRemovedFromBlueCol = []
        for blueC in range(len(blueBoard[0])):
            isFull = True
            for blueR in range(len(blueBoard)):
                if blueBoard[blueR][blueC] == 0:
                    isFull = False
                    break
            if isFull:
                toBeRemovedFromBlueCol.append(blueC)

        for blocksToBeRemoved in toBeRemovedFromBlueCol:
            for blueR in range(len(blueBoard)):
                blueBoard[blueR][blocksToBeRemoved] = 0

            for blueC in range(blocksToBeRemoved, 0, -1):
                for blueR in range(len(blueBoard)):
                    blueBoard[blueR][blueC], blueBoard[blueR][blueC - 1] = \
                        blueBoard[blueR][blueC - 1], blueBoard[blueR][blueC]

        # In case there's any block in 0, 1 cols in the blue board
        maxNumOfBlueBlocksInZeroOne = 0
        for blueR in range(len(blueBoard)):
            curNumOfBlueBlocks = 0
            for blueC in range(1, -1, -1):
                if blueBoard[blueR][blueC] == 1:
                    curNumOfBlueBlocks += 1
            maxNumOfBlueBlocksInZeroOne = max(maxNumOfBlueBlocksInZeroOne, curNumOfBlueBlocks)

        if maxNumOfBlueBlocksInZeroOne > 0:
            for blueC in range(len(blueBoard[0]) - 1 - maxNumOfBlueBlocksInZeroOne, -1, -1):
                for blueR in range(len(blueBoard)):
                    blueBoard[blueR][blueC + maxNumOfBlueBlocksInZeroOne] = blueBoard[blueR][blueC]

            for blueC in range(maxNumOfBlueBlocksInZeroOne):
                for blueR in range(len(blueBoard)):
                    blueBoard[blueR][blueC] = 0

        # Check the green board
        if t == 1:
            lastRow = -1
            for greenR in range(len(greenBoard)):
                if greenBoard[greenR][c] == 0:
                    lastRow = greenR
                else:
                    break
            greenBoard[lastRow][c] = 1

        elif t == 2:
            lastRow = -1
            for greenR in range(len(greenBoard)):
                if greenBoard[greenR][c] == 0 and greenBoard[greenR][c + 1] == 0:
                    lastRow = greenR
                else:
                    break
            greenBoard[lastRow][c] = 1
            greenBoard[lastRow][c + 1] = 1

        elif t == 3:
            lastRow = -1
            for greenR in range(1, len(greenBoard)):
                if greenBoard[greenR][c] == 0 and greenBoard[greenR - 1][c] == 0:
                    lastRow = greenR
                else:
                    break
            greenBoard[lastRow][c] = 1
            greenBoard[lastRow - 1][c] = 1

        toBeRemovedFromGreenRow = []
        for greenR in range(len(greenBoard)):
            isFull = True
            for greenC in range(len(greenBoard[0])):
                if greenBoard[greenR][greenC] == 0:
                    isFull = False
                    break
            if isFull:
                toBeRemovedFromGreenRow.append(greenR)

        for blocksToBeRemoved in toBeRemovedFromGreenRow:
            for greenC in range(len(greenBoard[0])):
                greenBoard[blocksToBeRemoved][greenC] = 0

            for greenR in range(blocksToBeRemoved, 0, -1):
                greenBoard[greenR], greenBoard[greenR - 1] = greenBoard[greenR - 1], greenBoard[greenR]

        # In case there's any block in 0, 1 rows in the green board
        maxNumOfGreenBlocksInZeroOne = 0
        for greenC in range(len(greenBoard[0])):
            curNumOfGreenBlocks = 0
            for greenR in range(2):
                if greenBoard[greenR][greenC] == 1:
                    curNumOfGreenBlocks += 1
            maxNumOfGreenBlocksInZeroOne = max(maxNumOfGreenBlocksInZeroOne, curNumOfGreenBlocks)

        if maxNumOfGreenBlocksInZeroOne > 0:
            for greenR in range(len(greenBoard) - 1 - maxNumOfGreenBlocksInZeroOne, -1, -1):
                for greenC in range(len(greenBoard[0])):
                    greenBoard[greenR + maxNumOfGreenBlocksInZeroOne][greenC] = greenBoard[greenR][greenC]

            for greenR in range(2):
                for greenC in range(len(greenBoard[0])):
                    greenBoard[greenR][greenC] = 0

        res += len(toBeRemovedFromBlueCol) + len(toBeRemovedFromGreenRow)

        # print("blue")
        # for blueR in range(len(blueBoard)):
        #     print(blueBoard[blueR])
        #
        # print("green")
        # for greenR in range(len(greenBoard)):
        #     print(greenBoard[greenR])

    numOfBlocks = 0
    for blueR in range(len(blueBoard)):
        for blueC in range(len(blueBoard[0])):
            if blueBoard[blueR][blueC] == 1:
                numOfBlocks += 1

    for greenR in range(len(greenBoard)):
        for greenC in range(len(greenBoard[0])):
            if greenBoard[greenR][greenC] == 1:
                numOfBlocks += 1

    return [res, numOfBlocks]

result = solve()
for i in result:
    print(i)