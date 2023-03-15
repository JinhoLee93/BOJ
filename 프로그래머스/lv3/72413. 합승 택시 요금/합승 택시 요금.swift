import Foundation

func solution(_ n:Int, _ s:Int, _ a:Int, _ b:Int, _ fares:[[Int]]) -> Int {
    var res = Int.max
    var graph: [Int:[(Int, Int)]] = [:]
    for f in fares {
        var s = f[0], d = f[1], w = f[2]
        graph[s, default: []].append((d, w))
        graph[d, default: []].append((s, w))
    }
    
    func dijkstra(_ src: Int) -> [Int] {
        var q = [(src, 0)]
        var distMap = Array(repeating: Int.max, count: n + 1) 
        distMap[src] = 0
        while !q.isEmpty { 
            var cur = q.removeFirst()
            var s = cur.0, w = cur.1
            if distMap[s] < w {
                continue
            }
            guard let g = graph[s] else { continue }
            for n in g {
                var d = n.0, nw = n.1 + w
                if distMap[d] <= nw {
                    continue
                }
                distMap[d] = nw
                q.append((d, nw))
            }
        }
        
        return distMap
    }
    
    for i in 1..<n + 1 {
        var dist = dijkstra(i)
        var s = dist[s], a = dist[a], b = dist[b]
        if s != Int.max && a != Int.max && b != Int.max {
            res = min(res, s + a + b)
        }
    }
    
    return res
}