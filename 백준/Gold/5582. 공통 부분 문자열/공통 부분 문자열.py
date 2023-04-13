f = input()
s = input()

F, S = len(f), len(s)
dp = [[0] * (S + 1) for _ in range(F + 1)]

res = 0
for i in range(F - 1, -1, -1):
    for j in range(S - 1, -1, -1):
        if f[i] == s[j]:
            dp[i][j] = 1 + dp[i + 1][j + 1]
            res = max(res, dp[i][j])
print(res)