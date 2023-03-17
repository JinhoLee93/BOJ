import Foundation

func solution(_ info:[Int], _ edges:[[Int]]) -> Int {
    var res = 0
    var graph: [Int:[Int]] = [:]
    for e in edges {
        var src = e[0], dest = e[1]
        graph[src, default: []].append(dest) 
        graph[dest, default: []].append(src) 
    }
    
    var visited: Set<Int> = []
    func backtrack(_ dest: Int, _ sheep: Int, _ wolf: Int, _ beginning: Bool, _ temp: inout [Int]) {
        guard let g = graph[dest] else { return }
        if (sheep <= wolf && !beginning) || visited.contains(dest) {
             
            return
        }
        
        visited.insert(dest)
        for n in g {
            temp.append(n)
        }
        for nn in temp {
            if info[dest] == 0 {
                backtrack(nn, sheep + 1, wolf, false, &temp)
                res = max(res, sheep + 1)
            } else {
                backtrack(nn, sheep, wolf + 1, false, &temp)
            }
        }
        for n in g {
            temp.popLast()
        }
        visited.remove(dest)
    }
    
    var temp: [Int] = []
    backtrack(0, 0, 0, true, &temp)
    
    return res
}