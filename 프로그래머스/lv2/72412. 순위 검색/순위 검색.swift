import Foundation

func solution(_ info:[String], _ query:[String]) -> [Int] {
    var res = Array(repeating: 0, count: query.count)
    var list: [[String]:[Int]] = [:]
    
    func backtrack(_ i: Int, _ s: Int, _ temp: inout [String]) {
        if i == 4 {
            list[temp, default: []].append(s)
            
            return
        }
        
        var t = temp[i]
        temp[i] = "-"
        backtrack(i + 1, s, &temp)
        temp[i] = t
        backtrack(i + 1, s, &temp)
    }
    
    for i in info {
        var tokens = i.split(separator: " ").map { String($0) }
        var score = Int(tokens.popLast()!)!
        backtrack(0, score, &tokens)
    }
    
    for k in list.keys {
        list[k]!.sort()
    }
    
    for i in 0..<query.count {
        var q = query[i]
        var tokens = q.split(separator: " ").filter { $0 != "and" }.map { String($0) }
        var score = Int(tokens.popLast()!)!
        guard let curList = list[tokens] else { continue }
        var l = 0, r = curList.count - 1
        while l <= r {
            var mid = (r + l) / 2
            if curList[mid] >= score {
                r = mid - 1
            } else {
                l = mid + 1
            }
        }
        res[i] = curList.count - l
    }
    
    return res
}