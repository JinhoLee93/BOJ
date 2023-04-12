import sys

N, M = list(map(int, input().strip().split()))
K = int(input())
empty = set()
for _ in range(K):
    e = tuple(map(int, sys.stdin.readline().strip().split()))
    e = (e[0] - 1, e[1] - 1)
    empty.add(e)

res = 0
dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[N - 1][M - 1] = 1

for c in range(M - 1, -1, -1):
    for r in range(N - 1, -1, -1):
        if (r, c) == (N - 1, M - 1) or (r, c) in empty:
            continue
        adder = dp[r + 1][c]
        if c % 2 == 0:
            adder += dp[r][c + 1] + dp[r - 1][c + 1]
        else:
            adder += dp[r][c + 1] + dp[r + 1][c + 1]
        dp[r][c] = adder
print(dp[0][0] % ((10 ** 9) + 7))