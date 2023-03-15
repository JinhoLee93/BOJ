import Foundation

func solution(_ info:[Int], _ edges:[[Int]]) -> Int {
    var res = Int.min
    var graph: [Int:[Int]] = [:]
    for e in edges {
        var src = e[0], dest = e[1] 
        graph[src, default: []].append(dest)
        graph[dest, default: []].append(src)
    }
    
    var visited: Set<Int> = []
    func backtrack(_ dest: Int, _ s: Int, _ w: Int, _ start: Bool, _ temp: inout [Int]) {
        guard let n = graph[dest] else { return }
        if (w >= s && !start) || visited.contains(dest) {
            
            return
        }
        
        visited.insert(dest)
        for nn in n {
            temp.append(nn)
        }
        for next in temp {
            if info[dest] == 0 {
                backtrack(next, s + 1, w, false, &temp)
                res = max(res, s + 1)
            } else {
                backtrack(next, s, w + 1, false, &temp)
            }
        }
        for nn in n {
            temp.popLast()
        }
        visited.remove(dest)
    }
    
    var temp: [Int] = []
    backtrack(0, 0, 0, true, &temp)
    
    return res
}