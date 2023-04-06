N, K = list(map(int, input().strip().split()))
belt = list(map(int, input().strip().split()))
cellsWithRobot = [False] * N
robots = []
busted = 0
for i in range(2 * N):
    if belt[i] == 0:
        busted += 1

process = 1
while busted < K:
    # Move the Belt
    toBeAddedAtFirst = belt.pop()
    belt = [toBeAddedAtFirst] + belt

    toBePopped = 0
    for i in range(len(robots)):
        curIdx = robots[i]
        nxtIdx = curIdx + 1

        # Move the Belt
        if nxtIdx == N - 1:
            cellsWithRobot[curIdx] = False
            toBePopped += 1
            continue
        else:
            cellsWithRobot[curIdx] = False
            robots[i] = nxtIdx
            cellsWithRobot[nxtIdx] = True

        curIdx = robots[i]
        nxtIdx = curIdx + 1

        # Move the Robots
        if cellsWithRobot[nxtIdx]:
            robots[i] = curIdx
        else:
            if belt[nxtIdx] > 0:
                if nxtIdx == N - 1:
                    toBePopped += 1
                    cellsWithRobot[curIdx] = False
                else:
                    cellsWithRobot[curIdx] = False
                    cellsWithRobot[nxtIdx] = True
                    robots[i] = nxtIdx
                belt[nxtIdx] -= 1
                if belt[nxtIdx] == 0:
                    busted += 1
                    if busted >= K:
                        print(f"{process}")
                        exit(0)
            else:
                robots[i] = curIdx

    for i in range(toBePopped):
        robots.pop(0)

    # Load a Robot
    if belt[0] > 0:
        robots.append(0)
        cellsWithRobot[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            busted += 1

    if busted >= K:
        print(f"{process}")
        exit(0)

    process += 1