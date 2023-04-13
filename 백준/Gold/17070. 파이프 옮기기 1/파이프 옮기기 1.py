def dfs(r, c, state):
    global res
    if (r, c) == (N - 1, N - 1):
        res += 1

        return

    if 0 <= r < N and 0 <= c < N and board[r][c] == 0:
        if state == "H":
            if 0 <= r < N and 0 <= c + 1 < N and board[r][c + 1] == 0:
                dfs(r, c + 1, "H")
            if 0 <= r + 1 < N and 0 <= c + 1 < N and board[r + 1][c + 1] == 0:
                if board[r + 1][c] == 0 and board[r][c + 1] == 0:
                    dfs(r + 1, c + 1, "D")
        elif state == "V":
            if 0 <= r + 1 < N and 0 <= c < N and board[r + 1][c] == 0:
                dfs(r + 1, c, "V")
            if 0 <= r + 1 < N and 0 <= c + 1 < N and board[r + 1][c + 1] == 0:
                if board[r + 1][c] == 0 and board[r][c + 1] == 0:
                    dfs(r + 1, c + 1, "D")
        else:
            if 0 <= r + 1 < N and 0 <= c + 1 < N and board[r + 1][c + 1] == 0:
                if board[r + 1][c] == 0 and board[r][c + 1] == 0:
                    dfs(r + 1, c + 1, "D")
            if 0 <= r < N and 0 <= c + 1 < N and board[r][c + 1] == 0:
                dfs(r, c + 1, "H")
            if 0 <= r + 1 < N and 0 <= c < N and board[r + 1][c] == 0:
                dfs(r + 1, c, "V")

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

if board[N - 1][N - 1] == 1:
    print(0)
    exit(0)

res = 0
dfs(0, 1, "H")

print(res)