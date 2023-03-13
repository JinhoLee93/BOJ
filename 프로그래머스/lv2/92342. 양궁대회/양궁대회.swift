import Foundation

func solution(_ n:Int, _ info:[Int]) -> [Int] {
    var res: [Int] = [-1]
    var totalArrows = n
    var oppo = info
    
    var maxDiff = 1, minScore = Int.max
    func backtrack(_ i: Int, _ arrows: Int, _ temp: inout [Int]) {
        if i == 11 {
            if arrows == totalArrows {
                var mySum = 0, oppoSum = 0, curTotalScore = 0
                for j in 0..<11 {
                    if temp[j] == 0 && oppo[j] == 0 {
                        continue
                    }

                    var curScore = 10 - j
                    curTotalScore += curScore * temp[j]
                    if temp[j] > oppo[j] {
                        mySum += curScore
                    } else {
                        oppoSum += curScore
                    }
                }

                var diff = mySum - oppoSum
                if maxDiff <= diff {
                    if maxDiff == diff {
                        if curTotalScore < minScore {
                            minScore = curTotalScore
                            res = temp
                        }
                    } else {
                        maxDiff = diff
                        res = temp
                        minScore = curTotalScore
                    }
                }
            }
            
            return
        }
        
        if temp[i] <= oppo[i] {
            temp[i] += 1
            backtrack(i, arrows + 1, &temp)
            temp[i] -= 1
        }
        backtrack(i + 1, arrows, &temp)
    }
    
    var temp = Array(repeating: 0, count: 11)
    backtrack(0, 0, &temp)
    
    return res
} 