import Foundation

func solution(_ n:Int, _ paths:[[Int]], _ gates:[Int], _ summits:[Int]) -> [Int] {
    var graph: [Int:[(Int, Int)]] = [:]
    for p in paths {
        var src = p[0], dest = p[1], intensity = p[2]
        graph[src, default: []].append((dest, intensity))
        graph[dest, default: []].append((src, intensity))
    }
    
    for key in graph.keys {
        graph[key]!.sort { $0.1 < $1.1 }
    }
    
    var minIntensity = Int.max, pairForMin = 0, intensities: [Int:Int] = [:]
    var summits = summits.sorted(), summitsSet = Set(summits), gates: Set<Int> = Set(gates)
    func dfs(_ summit: Int, _ dest: Int, _ curIntensity: Int) {
        if !intensities.keys.contains(dest) {
            intensities[dest] = curIntensity
        } else {
            if intensities[dest]! > curIntensity {
                intensities[dest] = curIntensity
            } else {
                
                return
            }
        }
        
        if gates.contains(dest) {
            minIntensity = curIntensity
            pairForMin = summit

            return
        }
        
        guard let g = graph[dest] else { return }
        for n in g {
            var newDest = n.0, intensity = n.1
            if summitsSet.contains(newDest) || intensity >= minIntensity {
                continue
            }
            dfs(summit, newDest, max(curIntensity, intensity))
        }
    }
    
    for s in summits {
        guard let cur = graph[s] else { continue }
        for c in cur {
            var nextNode = c.0, nextInt = c.1
            if summitsSet.contains(nextNode) || nextInt >= minIntensity {
                continue
            }
            intensities = [:]
            dfs(s, nextNode, nextInt)
        }
    }
        
    return [pairForMin, minIntensity]
}