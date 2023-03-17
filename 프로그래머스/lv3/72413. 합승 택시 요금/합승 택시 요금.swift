import Foundation

func solution(_ n:Int, _ s:Int, _ a:Int, _ b:Int, _ fares:[[Int]]) -> Int {
    var distMap = Array(repeating: Array(repeating: Int.max, count: n + 1), count: n + 1)
    
    for f in fares {
        var src = f[0], dest = f[1], cost = f[2] 
        distMap[src][dest] = cost
        distMap[dest][src] = cost
    }
    
    for i in 1..<n + 1 {
        distMap[i][i] = 0 
    }
    
    for i in 1..<n + 1 {
        for j in 1..<n + 1 {
            for k in 1..<n + 1 {
                var n1 = distMap[j][i], n2 = distMap[i][k]
                if n1 != Int.max && n2 != Int.max {
                    distMap[j][k] = min(distMap[j][k], n1 + n2)
                }
            }
        }
    }
    
    var res = Int.max
    for i in 1..<n + 1 {
        var s = distMap[i][s], a = distMap[i][a], b = distMap[i][b]
        if s != Int.max && a != Int.max && b != Int.max {
            res = min(res, s + a + b)
        }
    }
    
    return res
}