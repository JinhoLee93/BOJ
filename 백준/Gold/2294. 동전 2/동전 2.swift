var nk = readLine()!.split(separator: " ").map { Int($0)! }
var n = nk[0], k = nk[1]
var coins: [Int] = []
for _ in 0..<n {
    coins.append(Int(readLine()!)!)
}

var dp = Array(repeating: k + 1, count: k + 1)
dp[0] = 0
coins.sort()

for i in 1..<dp.count {
    for c in coins {
        if c > i {
            continue
        }
        dp[i] = min(dp[i], 1 + dp[i - c])
    }
}

var res = dp[k] == k + 1 ? -1 : dp[k]
print(res)