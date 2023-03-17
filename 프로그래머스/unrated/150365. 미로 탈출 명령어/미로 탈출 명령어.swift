import Foundation

func solution(_ n:Int, _ m:Int, _ x:Int, _ y:Int, _ r:Int, _ c:Int, _ k:Int) -> String {
    var R = n, C = m
    var dirs: [(Int, Int, String)] = [(0, -1, "l"), (0, 1, "r"), (-1, 0, "u"), (1, 0, "d")]
    dirs.sort { $0.2 < $1.2 }
    var q: [(Int, Int, String, Int)] = [(x, y, "", 0)]
    while !q.isEmpty {
        var cur = q.removeFirst()
        var curR = cur.0, curC = cur.1, curPath = cur.2, curDist = cur.3
        if curDist == k && (curR, curC) == (r, c) {
                
            return curPath
        }
        for d in dirs {
            var nextR = curR + d.0, nextC = curC + d.1
            if nextR > R || nextC > C || nextR < 1 || nextC < 1 {
                continue
            }
            var distToGoal = abs(r - nextR) + abs(c - nextC)
            if curDist + distToGoal + 1 > k {
                continue
            }
            var n = (nextR, nextC, curPath + d.2, curDist + 1)
            q.append(n)
            break
        }
    }
    
    return "impossible"
}