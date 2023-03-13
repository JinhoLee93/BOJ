import Foundation

func solution(_ queue1:[Int], _ queue2:[Int]) -> Int {
    var q = queue1 + queue2
    var total = q.reduce(0, +)
    guard total % 2 == 0 else { return -1 }
    var target = total / 2
    var curSum = queue1.reduce(0, +)
    var l = 0, r = queue1.count, count = 0
    while r < q.count {
        if curSum == target {
            
            return count
        } else if curSum < target {
            curSum += q[r]
            r += 1
        } else {
            curSum -= q[l]
            l += 1
        }
        count += 1
    }
    
    return -1
}