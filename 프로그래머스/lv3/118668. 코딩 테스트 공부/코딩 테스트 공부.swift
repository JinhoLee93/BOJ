import Foundation

func solution(_ alp:Int, _ cop:Int, _ problems:[[Int]]) -> Int {
    var maxAlp = 0, maxCop = 0
    for p in problems {
        maxAlp = max(maxAlp, p[0])
        maxCop = max(maxCop, p[1])
    }
    
    maxAlp = max(maxAlp, alp)
    maxCop = max(maxCop, cop)
    
    var dp = Array(repeating: Array(repeating: Int.max, count: maxCop + 1), count: maxAlp + 1)
    dp[alp][cop] = 0
    
    for a in alp..<maxAlp + 1 {
        for c in cop..<maxCop + 1 {
            if a + 1 <= maxAlp {
                dp[a + 1][c] = min(dp[a + 1][c], dp[a][c] + 1)
            }
            
            if c + 1 <= maxCop {
                dp[a][c + 1] = min(dp[a][c + 1], dp[a][c] + 1) 
            }

            for p in problems {
                var alpReq = p[0], copReq = p[1], alpRew = p[2], copRew = p[3], cost = p[4]
                if a >= alpReq && c >= copReq {
                    var curAlp = a + alpRew, curCop = c + copRew
                    if curAlp > maxAlp {
                        curAlp = maxAlp
                    }
                    
                    if curCop > maxCop {
                        curCop = maxCop
                    }
                    
                    dp[curAlp][curCop] = min(dp[curAlp][curCop], dp[a][c] + cost)
                }
            }
        }
    }
    
    return dp[maxAlp][maxCop]
}