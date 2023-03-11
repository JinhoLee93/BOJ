import sys

# N = r, M = c, # = wall, R = Red, B = Blue, O = Goal
# Return -1 if it's impossible for the red ball to get to the goal (0) before 10 tilts
def solve(N, M, fromInput):
    R, C = N, M
    board = fromInput
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    red, blue, goal = (-1, -1), (-1, -1), (-1, -1)
    for r in range(R):
        for c in range(C):
            if board[r][c] == "R":
                red = (r, c)
            elif board[r][c] == "B":
                blue = (r, c)
            elif board[r][c] == "O":
                goal = (r, c)

    q = [(red[0], red[1], blue[0], blue[1], 0)]

    visited = set()
    visited.add((red[0], red[1], blue[0], blue[1]))

    while q:
        cur = q.pop(0)
        redR, redC, blueR, blueC, curDist = cur[0], cur[1], cur[2], cur[3], cur[4]

        if curDist > 10:

            return -1

        if (redR, redC) == goal:
            if (blueR, blueC) != goal:

                return curDist
            else:
                continue

        for d in dir:
            curBoard = [row[:] for row in board]
            curBoard[red[0]][red[1]] = "."
            curBoard[blue[0]][blue[1]] = "."
            curBoard[redR][redC] = "R"
            curBoard[blueR][blueC] = "B"
            newRedR, newRedC, newBlueR, newBlueC = 0, 0, 0, 0
            blueInGoal, runsIntoBlue, runsIntoRed = False, False, False
            if d == [1, 0]:
                for r in range(redR + 1, R):
                    if curBoard[r][redC] == "#" or curBoard[r][redC] == "O":
                        break
                    elif curBoard[r][redC] == "B":
                        runsIntoBlue = True
                        break

                for r in range(blueR + 1, R):
                    if curBoard[r][blueC] == "#" or curBoard[r][blueC] == "O":
                        break
                    elif curBoard[r][blueC] == "R":
                        runsIntoRed = True
                        break

                if runsIntoBlue:
                    for r in range(blueR + 1, R):
                        if curBoard[r][blueC] == "#":
                            newBlueR = r - 1
                            newBlueC = blueC
                            newRedR = newBlueR - 1
                            newRedC = redC
                            break
                        elif curBoard[r][blueC] == "O":
                            blueInGoal = True
                            break
                elif runsIntoRed:
                    for r in range(redR + 1, R):
                        if curBoard[r][redC] == "#":
                            newRedR = r - 1
                            newRedC = redC
                            newBlueR = newRedR - 1
                            newBlueC = blueC
                            break
                        elif curBoard[r][redC] == "O":
                            blueInGoal = True
                            break
                else:
                    for r in range(redR + 1, R):
                        if curBoard[r][redC] == "#":
                            newRedR = r - 1
                            newRedC = redC
                            break
                        elif curBoard[r][redC] == "O":
                            newRedR = r
                            newRedC = redC
                            break

                    for r in range(blueR + 1, R):
                        if curBoard[r][blueC] == "#":
                            newBlueR = r - 1
                            newBlueC = blueC
                            break
                        elif curBoard[r][blueC] == "O":
                            blueInGoal = True
                            break

            elif d == [-1, 0]:
                for r in range(redR - 1, -1, -1):
                    if curBoard[r][redC] == "#" or curBoard[r][redC] == "O":
                        break
                    elif curBoard[r][redC] == "B":
                        runsIntoBlue = True
                        break

                for r in range(blueR - 1, -1, -1):
                    if curBoard[r][blueC] == "#" or curBoard[r][blueC] == "O":
                        break
                    elif curBoard[r][blueC] == "R":
                        runsIntoRed = True
                        break

                if runsIntoBlue:
                    for r in range(blueR - 1, -1, -1):
                        if curBoard[r][blueC] == "#":
                            newBlueR = r + 1
                            newBlueC = blueC
                            newRedR = newBlueR + 1
                            newRedC = redC
                            break
                        elif curBoard[r][blueC] == "O":
                            blueInGoal = True
                            break

                elif runsIntoRed:
                    for r in range(redR - 1, -1, -1):
                        if curBoard[r][redC] == "#":
                            newRedR = r + 1
                            newRedC = redC
                            newBlueR = newRedR + 1
                            newBlueC = blueC
                            break
                        elif curBoard[r][redC] == "O":
                            blueInGoal = True
                            break
                else:
                    for r in range(redR - 1, -1, -1):
                        if curBoard[r][redC] == "#":
                            newRedR = r + 1
                            newRedC = redC
                            break
                        elif curBoard[r][redC] == "O":
                            newRedR = r
                            newRedC = redC
                            break

                    for r in range(blueR - 1, -1, -1):
                        if curBoard[r][blueC] == "#":
                            newBlueR = r + 1
                            newBlueC = blueC
                            break
                        elif curBoard[r][blueC] == "O":
                            blueInGoal = True
                            break

            elif d == [0, 1]:
                for c in range(redC + 1, C):
                    if curBoard[redR][c] == "#" or curBoard[redR][c] == "O":
                        break
                    elif curBoard[redR][c] == "B":
                        runsIntoBlue = True
                        break

                for c in range(blueC + 1, C):
                    if curBoard[blueR][c] == "#" or curBoard[blueR][c] == "O":
                        break
                    elif curBoard[blueR][c] == "R":
                        runsIntoRed = True
                        break

                if runsIntoBlue:
                    for c in range(blueC + 1, C):
                        if curBoard[blueR][c] == "#":
                            newBlueC = c - 1
                            newBlueR = blueR
                            newRedC = newBlueC - 1
                            newRedR = redR
                            break
                        elif curBoard[blueR][c] == "O":
                            blueInGoal = True
                            break
                elif runsIntoRed:
                    for c in range(redC + 1, C):
                        if curBoard[redR][c] == "#":
                            newRedC = c - 1
                            newRedR = redR
                            newBlueC = newRedC - 1
                            newBlueR = blueR
                            break
                        elif curBoard[redR][c] == "O":
                            blueInGoal = True
                            break
                else:
                    for c in range(redC + 1, C):
                        if curBoard[redR][c] == "#":
                            newRedC = c - 1
                            newRedR = redR
                            break
                        elif curBoard[redR][c] == "O":
                            newRedC = c
                            newRedR = redR
                            break

                    for c in range(blueC + 1, C):
                        if curBoard[blueR][c] == "#":
                            newBlueC = c - 1
                            newBlueR = blueR
                            break
                        elif curBoard[blueR][c] == "O":
                            blueInGoal = True
                            break

            else: # [0, -1]
                for c in range(redC - 1, -1, -1):
                    if curBoard[redR][c] == "#" or curBoard[redR][c] == "O":
                        break
                    elif curBoard[redR][c] == "B":
                        runsIntoBlue = True
                        break

                for c in range(blueC - 1, -1, -1):
                    if curBoard[blueR][c] == "#" or curBoard[blueR][c] == "O":
                        break
                    elif curBoard[blueR][c] == "R":
                        runsIntoRed = True
                        break

                if runsIntoBlue:
                    for c in range(blueC - 1, -1, -1):
                        if curBoard[blueR][c] == "#":
                            newBlueC = c + 1
                            newBlueR = blueR
                            newRedC = newBlueC + 1
                            newRedR = redR
                            break
                        elif curBoard[blueR][c] == "O":
                            blueInGoal = True
                            break
                elif runsIntoRed:
                    for c in range(redC - 1, -1, -1):
                        if curBoard[redR][c] == "#":
                            newRedC = c + 1
                            newRedR = redR
                            newBlueC = newRedC + 1
                            newBlueR = blueR
                            break
                        elif curBoard[redR][c] == "O":
                            blueInGoal = True
                            break
                else:
                    for c in range(redC - 1, -1, -1):
                        if curBoard[redR][c] == "#":
                            newRedC = c + 1
                            newRedR = redR
                            break
                        elif curBoard[redR][c] == "O":
                            newRedC = c
                            newRedR = redR
                            break

                    for c in range(blueC - 1, -1, -1):
                        if curBoard[blueR][c] == "#":
                            newBlueC = c + 1
                            newBlueR = blueR
                            break
                        elif curBoard[blueR][c] == "O":
                            blueInGoal = True
                            break

            if not blueInGoal:
                if not (newRedR, newRedC, newBlueR, newBlueC) in visited:
                    q.append((newRedR, newRedC, newBlueR, newBlueC, curDist + 1))
                    visited.add((newRedR, newRedC, newBlueR, newBlueC))

    return -1

N, M = map(int, input().split(" "))
fromInput = []
for _ in range(0, N):
    fromInput.append((list(input())))
print(solve(N, M, fromInput))
