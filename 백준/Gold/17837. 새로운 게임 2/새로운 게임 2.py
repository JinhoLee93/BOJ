N, K = list(map(int, input().split(" ")))
board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))

pieces = []
for i in range(K):
    pieces.append(list(map(int, input().split(" "))))
    for j in range(len(pieces[i])):
        pieces[i][j] -= 1

boardWithPieces = [[[] for _ in range(N)] for _ in range(N)]

for i in range(K):
    pieceR, pieceC = pieces[i][0], pieces[i][1]
    boardWithPieces[pieceR][pieceC].append(i)

def solve():
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for turn in range(1000):
        for i in range(len(pieces)):
            curPiece = pieces[i]
            curPieceR, curPieceC, curPieceDir = curPiece[0], curPiece[1], curPiece[2]
            moveTo, dirReversed = dirs[curPieceDir], False
            nxtPieceR, nxtPieceC = curPieceR + moveTo[0], curPieceC + moveTo[1]
            if nxtPieceR >= N or nxtPieceC >= N or nxtPieceR < 0 or nxtPieceC < 0:
                if curPieceDir == 0:
                    curPieceDir = 1
                elif curPieceDir == 1:
                    curPieceDir = 0
                elif curPieceDir == 2:
                    curPieceDir = 3
                else:
                    curPieceDir = 2
                dirReversed = True
                nxtMoveTo = dirs[curPieceDir]
                nxtPieceR, nxtPieceC = curPieceR + nxtMoveTo[0], curPieceC + nxtMoveTo[1]

            if board[nxtPieceR][nxtPieceC] == 0 or board[nxtPieceR][nxtPieceC] == 1:
                toBeMoved = []
                if len(boardWithPieces[curPieceR][curPieceC]) > 0:
                    maxlen = len(boardWithPieces[curPieceR][curPieceC])
                    idx = boardWithPieces[curPieceR][curPieceC].index(i)
                    toBeMoved = boardWithPieces[curPieceR][curPieceC][idx:maxlen]
                    boardWithPieces[curPieceR][curPieceC] = boardWithPieces[curPieceR][curPieceC][0:idx]

                for moving in toBeMoved:
                    if moving == i:
                        pieces[moving] = [nxtPieceR, nxtPieceC, curPieceDir]
                    else:
                        pieces[moving] = [nxtPieceR, nxtPieceC, pieces[moving][2]]
                    boardWithPieces[nxtPieceR][nxtPieceC].append(moving)

                if board[nxtPieceR][nxtPieceC] == 1:
                    maxlen = len(boardWithPieces[nxtPieceR][nxtPieceC])
                    idx = boardWithPieces[nxtPieceR][nxtPieceC].index(i)
                    prv = boardWithPieces[nxtPieceR][nxtPieceC][0:idx]
                    nxt = boardWithPieces[nxtPieceR][nxtPieceC][idx:maxlen]
                    nxt.reverse()
                    boardWithPieces[nxtPieceR][nxtPieceC] = prv + nxt
            else:
                if dirReversed:
                    pieces[i] = [curPieceR, curPieceC, curPieceDir]
                else:
                    if curPieceDir == 0:
                        curPieceDir = 1
                    elif curPieceDir == 1:
                        curPieceDir = 0
                    elif curPieceDir == 2:
                        curPieceDir = 3
                    else:
                        curPieceDir = 2
                    becauseBlueMoveTo = dirs[curPieceDir]
                    becauseBlueNxtR = curPieceR + becauseBlueMoveTo[0]
                    becauseBlueNxtC = curPieceC + becauseBlueMoveTo[1]
                    if becauseBlueNxtR >= N or becauseBlueNxtC >= N or becauseBlueNxtR < 0 or \
                        becauseBlueNxtC < 0 or board[becauseBlueNxtR][becauseBlueNxtC] == 2:
                        pieces[i] = [curPieceR, curPieceC, curPieceDir]
                        continue

                    toBeMoved = []
                    if len(boardWithPieces[curPieceR][curPieceC]) > 0:
                        maxlen = len(boardWithPieces[curPieceR][curPieceC])
                        idx = boardWithPieces[curPieceR][curPieceC].index(i)
                        toBeMoved = boardWithPieces[curPieceR][curPieceC][idx:maxlen]
                        boardWithPieces[curPieceR][curPieceC] = boardWithPieces[curPieceR][curPieceC][0:idx]

                    for moving in toBeMoved:
                        if moving == i:
                            pieces[moving] = [becauseBlueNxtR, becauseBlueNxtC, curPieceDir]
                        else:
                            pieces[moving] = [becauseBlueNxtR, becauseBlueNxtC, pieces[moving][2]]
                        boardWithPieces[becauseBlueNxtR][becauseBlueNxtC].append(moving)

                    if board[becauseBlueNxtR][becauseBlueNxtC] == 1:
                        maxlen = len(boardWithPieces[becauseBlueNxtR][becauseBlueNxtC])
                        idx = boardWithPieces[becauseBlueNxtR][becauseBlueNxtC].index(i)
                        prv = boardWithPieces[becauseBlueNxtR][becauseBlueNxtC][0:idx]
                        nxt = boardWithPieces[becauseBlueNxtR][becauseBlueNxtC][idx:maxlen]
                        nxt.reverse()
                        boardWithPieces[becauseBlueNxtR][becauseBlueNxtC] = prv + nxt

            for r in range(N):
                for c in range(N):
                    if len(boardWithPieces[r][c]) >= 4:

                        return turn + 1

    return -1

print(solve())