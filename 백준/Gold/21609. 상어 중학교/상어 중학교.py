def solve(N, numOfColors, grid):
    res = 0
    def dfs(r, c, color, localVisited):
        if r >= N or c >= N or r < 0 or c < 0 or \
            (r, c) in visited or grid[r][c] == -1 or \
            grid[r][c] == -5 or (r, c, grid[r][c]) in localVisited:

            return

        if grid[r][c] != color and grid[r][c] != 0:

            return

        if grid[r][c] != 0:
            visited.add((r, c))
        localVisited.add((r, c, grid[r][c]))
        dfs(r + 1, c, color, localVisited)
        dfs(r - 1, c, color, localVisited)
        dfs(r, c + 1, color, localVisited)
        dfs(r, c - 1, color, localVisited)

    while True:
        blackBlocks, rainbowBlocks = [], []
        blockGroups, visited = [], set()
        # Get all the block groups
        for r in range(N):
            for c in range(N):
                if grid[r][c] == -1:
                    blackBlocks.append((r, c))
                elif grid[r][c] == 0:
                    rainbowBlocks.append((r, c))
                elif (r, c) not in visited:
                    localVisited = set()
                    dfs(r, c, grid[r][c], localVisited)
                    if len(localVisited) >= 2:
                        curGroup = list(localVisited)
                        curGroup.sort(key=lambda x:(-x[2], x[0], x[1]))
                        blockGroups.append(curGroup)

        if len(blockGroups) == 0:
            break

        blockGroups.sort(key=lambda x: -len(x))
        # print("group", blockGroups)

        maxRainbow, maxLen = 0, len(blockGroups[0])
        rainbowCandidates = []
        # How many rainbows
        for block in blockGroups:
            if len(block) == maxLen:
                curRainbow = 0
                for r, c, v in block:
                    if v == 0:
                        curRainbow += 1

                if maxRainbow < curRainbow:
                    rainbowCandidates = []
                    maxRainbow = curRainbow
                    rainbowCandidates.append(block)
                elif maxRainbow == curRainbow:
                    rainbowCandidates.append(block)
            else:
                break

        # print("rainbow", rainbowCandidates)
        candidates = []
        if len(rainbowCandidates) > 1:
            maxRow = rainbowCandidates[0][0][0]
            for block in rainbowCandidates:
                for r, c, v in block:
                    if v == 0:
                        break
                    if maxRow < r:
                        candidates = []
                        maxRow = r
                        candidates.append(block)
                        break
                    elif maxRow == r:
                        candidates.append(block)
                        break
        else:
            candidates.append(rainbowCandidates[0])

        # print("candidate", candidates)
        soonToBeRemoved = []
        if len(candidates) > 1:
            maxCol = candidates[0][0][1]
            for block in candidates:
                for b in block:
                    if b[2] == 0:
                        break
                    if maxCol < b[1]:
                        maxCol = b[1]
                        soonToBeRemoved = block
                        break
                    elif maxCol == b[1]:
                        soonToBeRemoved = block
                        break
        else:
            soonToBeRemoved = candidates[0]

        # print("soon", soonToBeRemoved)

        # Remove the biggest block group from the grid
        for r, c, _ in soonToBeRemoved:
            grid[r][c] = -5

        res += len(soonToBeRemoved) ** 2
        # print(res)
        # Apply gravity to the grid
        grid = applyGravity(grid)

        # Rotate 90 counterclockwise
        grid = rotate90DegreeCounterclockwise(grid)

        # Apply gravity again
        grid = applyGravity(grid)

        # print("after Gravity")
        # for i in range(N):
        #     print(grid[i])

    return res

def applyGravity(grid):
    for c in range(N):
        blocksToMove = []
        for r in range(N):
            if grid[r][c] > -1:
                blocksToMove.append((grid[r][c], r))
            elif grid[r][c] == -1:
                for nextR in range(1, len(blocksToMove) + 1):
                    cur = blocksToMove.pop()
                    grid[cur[1]][c] = -5
                    grid[r - nextR][c] = cur[0]
                blocksToMove = []

            if r == N - 1 and grid[r][c] != -1:
                for nextR in range(len(blocksToMove)):
                    cur = blocksToMove.pop()
                    grid[cur[1]][c] = -5
                    grid[r - nextR][c] = cur[0]

    return grid

def rotate90DegreeCounterclockwise(grid):
    newGrid = []
    for c in range(N - 1, -1, -1):
        newRow = []
        for r in range(N):
            newRow.append(grid[r][c])
        newGrid.append(newRow)

    return newGrid

N, numOfColors = list(map(int, input().split(" ")))
grid = []

for _ in range(N):
    grid.append(list(map(int, input().split(" "))))

# print("init")
# for i in range(N):
#     print(grid[i])


print(solve(N, numOfColors, grid))