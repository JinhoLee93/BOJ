from collections import deque
import copy

N, M = list(map(int,input().strip().split()))
board = []
for _ in range(N):
    board.append(list(map(int, input().strip().split())))

def solve():
    def backtrack(i, temp):
        if len(temp) == M:
            combs.append(temp.copy())

            return

        if i == len(placeable):
            return

        temp.append(placeable[i])
        backtrack(i + 1, temp)
        temp.pop()
        backtrack(i + 1, temp)

    def bfs(c, board, numOfZeroes):
        time, q = 0, deque([])
        visited = set()
        for v in c:
            vr, vc, t = v[0], v[1], 1
            board[vr][vc] = t
            q.append((vr, vc, t))
            visited.add((vr, vc))

        while q:
            curR, curC, curT = q.popleft()
            board[curR][curC] = curT
            for d in dirs:
                nxtR, nxtC = curR + d[0], curC + d[1]
                if nxtR < 0 or nxtC < 0 or nxtR >= N or nxtC >= N or \
                        board[nxtR][nxtC] == -1 or (nxtR, nxtC) in visited:
                    continue
                visited.add((nxtR, nxtC))
                q.append((nxtR, nxtC, curT + 1))
                time = max(time, curT)
                if board[nxtR][nxtC] == 0:
                    numOfZeroes -= 1
                    if numOfZeroes == 0:
                        return time

                if time >= res:
                    return res

        return -1

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    placeable = []
    numOfZeroes = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                numOfZeroes += 1
            elif board[r][c] == 2:
                placeable.append((r, c))
            board[r][c] *= -1

    if numOfZeroes == 0:
        print(f"{0}")
        exit(0)

    combs = []
    backtrack(0, [])
    res = float("inf")

    for c in combs:
        newBoard = copy.deepcopy(board)
        curRes = bfs(c, newBoard, numOfZeroes)
        if curRes == -1:
            continue
        res = min(res, curRes)

    print(f"{-1}" if res == float("inf") else f"{res}")

solve()