import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var participants = stages.count, s: [Int:Int] = [:], res: [(Double, Int)] = []
    for i in 1..<N+2 {
        s[i] = 0
    }
    
    for p in stages {
        s[p]! += 1
    }
    
    for i in 1..<N+1 {
        var rate: Double = Double(s[i]!) / Double(participants)
        res.append((rate, i))
        participants -= s[i]! 
    }
    
    return res.sorted { $0.0 > $1.0 }.map { Int($0.1) }
}