from collections import deque
N, K = list(map(int, input().strip().split()))

beltArr = list(map(int, input().strip().split()))
firstHalf = beltArr[:N]
secondHalf = beltArr[N:]

belt = deque(firstHalf + secondHalf)
cellsWithRobot = deque([False] * 2 * N)

robots = {}
busted = 0
for i in range(2 * N):
    if belt[i] == 0:
        busted += 1

process, robotNumber = 1, 0
while busted < K:
    # Move the Belt
    toBeAddedAtFirst = belt.pop()
    toBeAddedAtFirstCell = cellsWithRobot.pop()
    belt.appendleft(toBeAddedAtFirst)
    cellsWithRobot.appendleft(toBeAddedAtFirstCell)
    newRobotsAfterBeltMoves = {}
    for robot in robots:
        robots[robot] += 1
        if robots[robot] == N - 1:
            cellsWithRobot[N - 1] = False
            continue
        else:
            newRobotsAfterBeltMoves[robot] = robots[robot]
    robots = newRobotsAfterBeltMoves

    # Move the Robots
    newRobotsAfterRobotsMove = {}
    for robot in sorted(robots.keys()):
        curIdx = robots[robot]
        nxtIdx = curIdx + 1
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
            else:
                newRobotsAfterRobotsMove[robot] = curIdx
    robots = newRobotsAfterRobotsMove

    if busted >= K:
        break

    # Load a Robot
    if belt[0] > 0:
        robots[robotNumber] = 0
        cellsWithRobot[0] = True
        robotNumber += 1
        belt[0] -= 1
        if belt[0] == 0:
            busted += 1

    if busted >= K:
        break

    process += 1

print(f"{process}")