import sys

N, K = list(map(int, input().split(" ")))
contents = []
for _ in range(N):
    contents.append(list(map(int, input().split(" "))))

contents.sort(key=lambda x:x[0])

def solve():
    dp = [[0 for _ in range(K + 1)] for _ in range(len(contents) + 1)]
    maximum = 0
    for i in range(1, len(contents) + 1):
        for j in range(1, K + 1):
            idx = i - 1
            w = contents[idx][0]
            v = contents[idx][1]
            if j - w < 0:
                dp[i][j] = dp[i - 1][j]
                continue
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            maximum = max(maximum, dp[i][j])

    return maximum

print(solve())
