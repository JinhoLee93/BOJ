import sys
import copy
sys.setrecursionlimit(10**6)

N = 4
board = [[] for _ in range(N)]
fishList = {}
for i in range(N):
    infoForRow = list(map(int, input().split(" ")))
    for c in range(0, 8, 2):
        curFishNum, curFishDir = infoForRow[c], infoForRow[c + 1]
        fish = [infoForRow[c], infoForRow[c + 1] - 1]
        board[i].append(fish)
        col = c // 2
        fishList[fish[0]] = [i, col, fish[1]]

def solve():
    res = 0
    N = 4
    # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
    fishDirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    curSharkPos = [0, 0]
    curSharkDir = board[curSharkPos[0]][curSharkPos[1]][1]

    # board element = [fishNumber, fishDir] -1 fishNum means the shark

    def dfs(board, fishList, curSharkPos, curSharkDir, sum):
        nonlocal res

        # The shark enters
        curSharkR, curSharkC = curSharkPos[0], curSharkPos[1]
        if board[curSharkR][curSharkC][0] > 0:
            sum += board[curSharkR][curSharkC][0]
            fishToBeEaten = board[curSharkR][curSharkC][0]
            curSharkDir = board[curSharkR][curSharkC][1]
            board[curSharkR][curSharkC] = [-1, curSharkDir]
            fishList.pop(fishToBeEaten)

        # The fish moves
        for curFishNum in range(1, 17):
            if curFishNum not in fishList.keys():
                continue
            curFish = fishList[curFishNum]
            curFishR, curFishC = curFish[0], curFish[1]
            # This cell is occupied by the shark or is empty.
            if curFishNum == -1 or curFishNum == 0:
                continue
            curFishDir = curFish[2]
            moveTo = fishDirs[curFishDir]
            nxtFishR, nxtFishC = curFishR + moveTo[0], curFishC + moveTo[1]
            while nxtFishR >= N or nxtFishC >= N or nxtFishR < 0 or nxtFishC < 0 or \
                    board[nxtFishR][nxtFishC][0] == -1:
                # Rotate counterclockwise
                curFishDir += 1
                if curFishDir > 7:
                    curFishDir = 0

                if curFishDir == board[curFishR][curFishC][1]:
                    break

                moveTo = fishDirs[curFishDir]
                nxtFishR, nxtFishC = curFishR + moveTo[0], curFishC + moveTo[1]
                # There's nowhere to go for the fish

            if board[nxtFishR][nxtFishC][0] > 0:
                nxtFish = board[nxtFishR][nxtFishC]
                nxtFishNum, nxtFishDir = nxtFish[0], nxtFish[1]
                fishList[nxtFishNum] = [curFishR, curFishC, nxtFishDir]
                board[curFishR][curFishC] = [nxtFishNum, nxtFishDir]
            elif board[nxtFishR][nxtFishC][0] == 0:
                board[curFishR][curFishC] = [0, 0]

            fishList[curFishNum] = [nxtFishR, nxtFishC, curFishDir]
            board[nxtFishR][nxtFishC] = [curFishNum, curFishDir]

        # the shark moves
        curSharkR, curSharkC = curSharkPos
        sharkMovesTo = fishDirs[curSharkDir]
        candidatesToBeEaten = []
        nxtSharkR, nxtSharkC = curSharkR + sharkMovesTo[0], curSharkC + sharkMovesTo[1]
        while nxtSharkR < N and nxtSharkC < N and nxtSharkR >= 0 and nxtSharkC >= 0:
            if board[nxtSharkR][nxtSharkC][0] > 0:
                candidatesToBeEaten.append(board[nxtSharkR][nxtSharkC][0])
            nxtSharkR += sharkMovesTo[0]
            nxtSharkC += sharkMovesTo[1]

        if not candidatesToBeEaten:
            res = max(res, sum)

            return

        for candidate in candidatesToBeEaten:
            board[curSharkR][curSharkC] = [0, 0]
            nxtSharkR, nxtSharkC, nxtSharkDir = fishList[candidate]
            dfs(copy.deepcopy(board), copy.deepcopy(fishList), [nxtSharkR, nxtSharkC], nxtSharkDir, sum)
            board[curSharkR][curSharkC] = [-1, curSharkDir]

    dfs(board, fishList, curSharkPos, curSharkDir, 0)

    return res

print(solve())