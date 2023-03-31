import sys

N, M, K = list(map(int, input().split(" ")))

resources = []
for _ in range(N):
    resources.append(list(map(int, sys.stdin.readline().split(" "))))

trees = [[{} for _ in range(N)] for _ in range(N) ]
for _ in range(M):
    r, c, age = list(map(int, input().split(" ")))
    trees[r - 1][c - 1][age] = 1

board = [[5 for _ in range(N)] for _ in range(N)]

def solve():
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for _ in range(K):
        for r in range(N):
            for c in range(N):
                if trees[r][c]:
                    deadTreesAboutToBeResources = 0
                    anyResourcesLeft = True
                    newTree = {}
                    for age in sorted(trees[r][c].keys()):
                        curResourcesTreesNeed = age * trees[r][c][age]
                        if not anyResourcesLeft:
                            deadTreesAboutToBeResources += (age // 2) * trees[r][c][age]
                            continue
                        if curResourcesTreesNeed <= board[r][c]:
                            board[r][c] -= age * trees[r][c][age]
                            newTree[age + 1] = trees[r][c][age]
                        else:
                            ableToFeed = board[r][c] // age
                            if ableToFeed == 0:
                                anyResourcesLeft = False
                                deadTreesAboutToBeResources += (age // 2) * trees[r][c][age]
                                continue
                            board[r][c] -= age * ableToFeed
                            newTree[age + 1] = ableToFeed
                            remainder = trees[r][c][age] - ableToFeed
                            deadTreesAboutToBeResources += (age // 2) * remainder
                    board[r][c] += deadTreesAboutToBeResources
                    trees[r][c] = newTree

        for r in range(N):
            for c in range(N):
                if trees[r][c]:
                    toBePopulated = 0
                    for age in trees[r][c]:
                        if age % 5 == 0:
                            toBePopulated += trees[r][c][age]

                    if toBePopulated > 0:
                        for _ in range(toBePopulated):
                            for d in dirs:
                                nxtR, nxtC = r + d[0], c + d[1]
                                if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= N:
                                    continue
                                if 1 in trees[nxtR][nxtC]:
                                    trees[nxtR][nxtC][1] += 1
                                else:
                                    trees[nxtR][nxtC][1] = 1
                board[r][c] += resources[r][c]

    res = 0
    for r in range(N):
        for c in range(N):
            res += sum(trees[r][c].values())

    print(res)

solve()