import Foundation

func solution(_ n:Int, _ s:Int, _ a:Int, _ b:Int, _ fares:[[Int]]) -> Int {
    var graph: [Int: [(Int, Int)]] = [:]
    for f in fares {
        var src = f[0], dest = f[1], cost = f[2]
        graph[src, default: []].append((dest, cost))
        graph[dest, default: []].append((src, cost))
    }
    
    func dijkstra(_ src: Int) -> [Int] {
        var distMap = Array(repeating: Int.max, count: n + 1)
        distMap[src] = 0
        var q: [(Int, Int)] = [(src, 0)]
        while !q.isEmpty {
            var cur = q.removeFirst()
            var dest = cur.0, cost = cur.1
            if distMap[dest] < cost {
                continue
            }
            guard let g = graph[dest] else { continue }
            for n in g {
                var newDest = n.0, newCost = n.1 + cost
                if distMap[newDest] < newCost {
                    continue
                }
                distMap[newDest] = newCost
                q.append((newDest, newCost))
            }
        }
        
        return distMap
    }
    
    var res = Int.max
    for src in 1..<n + 1 {
        var distMap = dijkstra(src)
        var s = distMap[s], a = distMap[a], b = distMap[b]
        if s != Int.max && a != Int.max && b != Int.max {
            res = min(res, s + a + b)
        }
    }
    
    return res
}