var N = Int(readLine()!)!
var eggs: [[Int]] = []
for _ in 0..<N {
    let egg = readLine()!.split(separator: " ").map { Int($0)! }
    eggs.append(egg)
}

func solve(_ N: Int, _ eggs: [[Int]]) {
    var res = 0, eggs = eggs
    func backtrack(_ i: Int, _ eggs: inout [[Int]]) {
        if i == N {
            var count = 0
            for egg in eggs {
                if egg[0] <= 0 {
                    count += 1
                }
            }
            
            res = max(res, count)
            
            return
        }
        
        if eggs[i][0] <= 0 {
            backtrack(i + 1, &eggs)
            
            return
        }
        
        var allCracked = true
        for j in 0..<N {
            if eggs[j][0] <= 0 || i == j {
                continue
            }
            allCracked = false
            eggs[i][0] -= eggs[j][1]
            eggs[j][0] -= eggs[i][1]
            backtrack(i + 1, &eggs)
            eggs[i][0] += eggs[j][1]
            eggs[j][0] += eggs[i][1]
        }
        
        if allCracked {
            backtrack(N, &eggs)
            
            return
        }
        
        return
    }
    
    backtrack(0, &eggs)
    
    print(res)
}

solve(N, eggs)
