var N = Int(readLine()!)!
for _ in 0..<N {
    var arr: [[Int]] = []
    let numOfCol = Int(readLine()!)!
    for _ in 0..<2 {
        let cur = readLine()!.split(separator: " ").map { Int($0)! }
        arr.append(cur)
    }
    var dp = Array(repeating: Array(repeating: Int.min, count: numOfCol + 1), count: 2)
    dp[0][0] = 0
    dp[1][0] = 0
    dp[0][1] = arr[0][0]
    dp[1][1] = arr[1][0]
    
    for c in 2..<numOfCol + 1 {
        dp[0][c] = max(dp[1][c - 1] + arr[0][c - 1], dp[1][c - 2] + arr[0][c - 1], dp[0][c - 2] + arr[0][c - 1])
        dp[1][c] = max(dp[0][c - 1] + arr[1][c - 1], dp[1][c - 2] + arr[1][c - 1], dp[0][c - 2] + arr[1][c - 1])
    }
    
    print(max(dp[0][numOfCol], dp[1][numOfCol]))
}