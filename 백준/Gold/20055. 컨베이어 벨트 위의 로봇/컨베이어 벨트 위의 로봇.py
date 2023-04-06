N, K = list(map(int, input().strip().split()))
belt = list(map(int, input().strip().split()))
cellsWithRobot = [False] * N
robots = {}
busted = 0
for i in range(2 * N):
    if belt[i] == 0:
        busted += 1

process, robotNumber = 1, 0
while busted < K:
    # Move the Belt
    toBeAddedAtFirst = belt.pop()
    belt = [toBeAddedAtFirst] + belt

    newRobotsAfterRobotsMove = {}
    for robot in sorted(robots.keys()):
        curIdx = robots[robot]
        nxtIdx = curIdx + 1

        # Move the Belt
        if nxtIdx == N - 1:
            cellsWithRobot[curIdx] = False
            continue
        else:
            cellsWithRobot[curIdx] = False
            robots[robot] = nxtIdx
            cellsWithRobot[nxtIdx] = True

        curIdx = robots[robot]
        nxtIdx = curIdx + 1

        # Move the Robots
        if cellsWithRobot[nxtIdx]:
            newRobotsAfterRobotsMove[robot] = curIdx
        else:
            if belt[nxtIdx] > 0:
                if nxtIdx == N - 1:
                    cellsWithRobot[curIdx] = False
                else:
                    cellsWithRobot[curIdx] = False
                    cellsWithRobot[nxtIdx] = True
                    newRobotsAfterRobotsMove[robot] = nxtIdx
                belt[nxtIdx] -= 1
                if belt[nxtIdx] == 0:
                    busted += 1
                    if busted >= K:
                        print(f"{process}")
                        exit(0)
            else:
                newRobotsAfterRobotsMove[robot] = curIdx
    robots = newRobotsAfterRobotsMove

    # Load a Robot
    if belt[0] > 0:
        robots[robotNumber] = 0
        cellsWithRobot[0] = True
        robotNumber += 1
        belt[0] -= 1
        if belt[0] == 0:
            busted += 1

    if busted >= K:
        print(f"{process}")
        exit(0)

    process += 1