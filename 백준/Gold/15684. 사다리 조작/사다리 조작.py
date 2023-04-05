from collections import defaultdict
N, M, H = list(map(int, input().split()))

lines = [[0 for _ in range(N + 1)] for _ in range(H + 1)]
for _ in range(M):
    row, startCol = list(map(int, input().split()))
    endCol = startCol + 1
    lines[row][startCol] = endCol
    lines[row][endCol] = startCol

def backtrack(i, times):
    global res
    if times >= res:

        return

    passed = True
    for c in range(1, N + 1):
        currentCol = c
        for r in range(1, H + 2):
            if r <= H:
                if lines[r][currentCol] != 0:
                    currentCol = lines[r][currentCol]

        if currentCol != c:
            passed = False
            break

    if passed:
        res = min(res, times)

        return

    if i == len(placeables):

        return

    if times < 3:
        toBeAddedR, toBeAddedStartCol = placeables[i]
        toBeAddedEndCol = toBeAddedStartCol + 1
        if lines[toBeAddedR][toBeAddedStartCol] == 0 and lines[toBeAddedR][toBeAddedEndCol] == 0:
            lines[toBeAddedR][toBeAddedStartCol] = toBeAddedEndCol
            lines[toBeAddedR][toBeAddedEndCol] = toBeAddedStartCol
            if i + 1 < len(placeables) and placeables[i + 1][1] == toBeAddedEndCol:
                backtrack(i + 2, times + 1)
            else:
                backtrack(i + 1, times + 1)
            lines[toBeAddedR][toBeAddedStartCol] = 0
            lines[toBeAddedR][toBeAddedEndCol] = 0
        backtrack(i + 1, times)

res = float("inf")
placeables = []
for r in range(1, H + 1):
    for c in range(1, N):
        if (r, c) in lines or (r, c + 1) in lines:
            continue
        placeables.append((r, c))

backtrack(0, 0)

if res == float("inf"):
    res = -1

print(f"{res}")