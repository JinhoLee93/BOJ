import sys
import math
import copy
from collections import deque
from collections import defaultdict
sys.setrecursionlimit(10**6)

N, M, K = list(map(int, input().split(" ")))
resources = []
for _ in range(N):
    resources.append(list(map(int, input().split(" "))))

trees = [[{} for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, age = list(map(int, sys.stdin.readline().split(" ")))
    trees[r - 1][c - 1][age] = 1

board = [[5 for _ in range(N)] for _ in range(N)]

def solve():
    for _ in range(K):
        for r in range(N):
            for c in range(N):
                dead = 0
                if trees[r][c]:
                    nxtTree = {}
                    wentBelowZero = False
                    for age in sorted(trees[r][c].keys()):
                        if wentBelowZero:
                            dead += (age // 2) * trees[r][c][age]
                            continue
                        if board[r][c] >= age * trees[r][c][age]:
                            nxtTree[age + 1] = trees[r][c][age]
                            board[r][c] -= age * trees[r][c][age]
                        else:
                            wentBelowZero = True
                            remaining = board[r][c] // age
                            if remaining == 0:
                                dead += (age // 2) * trees[r][c][age]
                                continue
                            board[r][c] -= age * remaining
                            dead += (age // 2) * (trees[r][c][age] - remaining)
                            nxtTree[age + 1] = remaining
                    trees[r][c] = nxtTree
                board[r][c] += resources[r][c] + dead

        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for r in range(N):
            for c in range(N):
                if trees[r][c]:
                    toPopulate = 0
                    for age in trees[r][c].keys():
                        if age % 5 == 0:
                            toPopulate += trees[r][c][age]

                    for d in dirs:
                        nxtR, nxtC = r + d[0], c + d[1]
                        if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= N:
                            continue
                        if 1 in trees[nxtR][nxtC]:
                            trees[nxtR][nxtC][1] += toPopulate
                        else:
                            trees[nxtR][nxtC][1] = toPopulate

    res = 0
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                res += sum(trees[r][c].values())

    print(res)

solve()