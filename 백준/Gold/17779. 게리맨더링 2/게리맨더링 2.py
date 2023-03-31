N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split(" "))))

def solve():
    d1Dir = [(1, -1), (-1, 1)]
    d2Dir = [(1, 1), (-1, -1)]
    res = float("inf")
    for r in range(N):
        for c in range(N):
            for d1 in range(1, (N // 2) + 1):
                for d2 in range(1, (N // 2) + 1):
                    failed = False
                    curR, curC = r, c
                    board = [[0 for _ in range(N)] for _ in range(N)]
                    for i in range(2):
                        curD1Dir = d1Dir[i]
                        for d in range(d1):
                            nxtR, nxtC = curR + curD1Dir[0], curC + curD1Dir[1]
                            if 0 <= nxtR < N and 0 <= nxtC < N:
                                board[nxtR][nxtC] = 5
                                curR, curC = nxtR, nxtC
                            else:
                                failed = True
                                break
                        if failed:
                            break

                        curD2Dir = d2Dir[i]
                        for d in range(d2):
                            nxtR, nxtC = curR + curD2Dir[0], curC + curD2Dir[1]
                            if 0 <= nxtR < N and 0 <= nxtC < N:
                                board[nxtR][nxtC] = 5
                                curR, curC = nxtR, nxtC
                            else:
                                failed = True
                                break
                        if failed:
                            break
                    if failed:
                        break

                    top, bottom = (r, c), (r + d1 + d2, c - d1 + d2)
                    left, right = (r + d1, c - d1), (r + d2, c + d2)
                    for u in range(r - 1, -1, -1):
                        board[u][c] = 1
                    for b in range(bottom[0] + 1, N):
                        board[b][bottom[1]] = 4
                    for l in range(left[1]):
                        board[left[0]][l] = 3
                    for ri in range(right[1] + 1, N):
                        board[right[0]][ri] = 2

                    for r1 in range(left[0]):
                        for c1 in range(N):
                            if board[r1][c1] != 0:
                                break
                            board[r1][c1] = 1

                    for r2 in range(right[0]):
                        for c2 in range(N - 1, -1, -1):
                            if board[r2][c2] != 0:
                                break
                            board[r2][c2] = 2

                    for r3 in range(left[0] + 1, N):
                        for c3 in range(N):
                            if board[r3][c3] != 0:
                                break
                            board[r3][c3] = 3

                    for r4 in range(N - 1, right[0], -1):
                        for c4 in range(N - 1, -1, -1):
                            if board[r4][c4] != 0:
                                break
                            board[r4][c4] = 4

                    for r5 in range(N):
                        for c5 in range(N):
                            if board[r5][c5] == 0:
                                board[r5][c5] = 5

                    p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0
                    for rp in range(N):
                        for cp in range(N):
                            if board[rp][cp] == 1:
                                p1 += A[rp][cp]
                            elif board[rp][cp] == 2:
                                p2 += A[rp][cp]
                            elif board[rp][cp] == 3:
                                p3 += A[rp][cp]
                            elif board[rp][cp] == 4:
                                p4 += A[rp][cp]
                            else:
                                p5 += A[rp][cp]

                    res = min(res, max(p1, p2, p3, p4, p5) - min(p1, p2, p3, p4, p5))
    print(res)
    
solve()