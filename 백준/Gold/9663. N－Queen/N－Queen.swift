import Foundation

var N = Int(readLine()!)!

func solve(_ N: Int) {
    var res = 0
    var col: [Bool] = Array(repeating: false, count: N)
    var leftDiag: [Bool] = Array(repeating: false, count: 2 * N - 1)
    var rightDiag: [Bool] = Array(repeating: false, count: 2 * N - 1)
    
    func backtrack(_ r: Int) {
        if r == N {
            res += 1
            
            return
        }
        
        for c in 0..<N {
            var left = r + c, right = c - r + (N - 1)
            if leftDiag[left] || rightDiag[right] || col[c] {
                continue
            }
            leftDiag[left] = true
            rightDiag[right] = true
            col[c] = true
            backtrack(r + 1)
            leftDiag[left] = false
            rightDiag[right] = false
            col[c] = false
        }
        
        return
    }
    
    backtrack(0)
    
    print(res)
    
    return
}

solve(N)