import Foundation

var nk = readLine()!.split(separator: " ").map { Int($0)! }
var n = nk[0], k = nk[1]
var coins: [Int] = []
for _ in 0..<n {
    coins.append(Int(readLine()!)!)
}

var dp = Array(repeating: 0, count: k + 1)
dp[0] = 1
coins.sort()

for c in coins {
    for l in stride(from: c, to: k + 1, by: 1) {
        if dp[l] + dp[l - c] >= Int(pow(2.0, 31.0)) {
            dp[l] = 0
        } else {
            dp[l] += dp[l - c]
        }
    }
}

print(dp[k])