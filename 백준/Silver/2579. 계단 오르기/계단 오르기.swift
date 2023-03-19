var N = Int(readLine()!)!
var stairs: [Int] = []
for _ in 0..<N {
    stairs.append(Int(readLine()!)!)
}

var dp: [String:Int] = [:]
func dfs(_ i: Int, _ consec: Int) -> Int {
    var key = "\(i) \(consec)"
    if dp.keys.contains(key) {
        
        return dp[key]!
    }
    
    if i < 0 || consec == 3 {
        
        return 0
    }
    
    dp[key] = max(dfs(i - 2, 1) + stairs[i], dfs(i - 1, consec + 1) + stairs[i])
    
    return dp[key]!
}

print(dfs(stairs.count - 1, 1))
