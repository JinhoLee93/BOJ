import sys
from collections import deque
from collections import defaultdict

N, M, K = list(map(int, input().split(" ")))
resources = [] # will be used during the winter
for _ in range(N):
    resources.append(list(map(int, input().split(" "))))

trees = defaultdict(deque)
for _ in range(M):
    tree = list(map(int, sys.stdin.readline().split(" ")))
    r, c, age = tree[0] - 1, tree[1] - 1, tree[2]
    trees[(r, c)].append(age)

board = [[5 for _ in range(N)] for _ in range(N)]

def solve(board, trees):
    for _ in range(K):
        # Spring, Summer
        for r in range(N):
            for c in range(N):
                key = (r, c)
                if key in trees:
                    r, c = key[0], key[1]
                    curTrees = trees[key]
                    breakPoint = -1
                    nxtTrees = deque()
                    for i in range(len(curTrees)):
                        if curTrees[i] > board[r][c]:
                            breakPoint = i
                            break
                        board[r][c] -= curTrees[i]
                        nxtTrees.append(curTrees[i] + 1)

                    if breakPoint != -1:
                        for i in range(breakPoint, len(curTrees)):
                            board[r][c] += curTrees[i] // 2
                    trees[key] = nxtTrees
                board[r][c] += resources[r][c]

        # Fall, Winter
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        newTrees = defaultdict(deque)
        for key in trees.keys():
            curTrees = trees[key]
            curR, curC = key[0], key[1]
            newTrees[key] += curTrees
            toPopulate = 0
            for curTree in curTrees:
                if curTree % 5 == 0:
                    toPopulate += 1
            for dir in dirs:
                nxtR, nxtC = curR + dir[0], curC + dir[1]
                if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= N:
                    continue
                for _ in range(toPopulate):
                    newTrees[(nxtR, nxtC)].appendleft(1)
        trees = newTrees

    res = 0
    for key in trees.keys():
        res += len(trees[key])

    print(res)

solve(board, trees)