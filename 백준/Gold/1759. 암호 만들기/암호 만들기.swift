import Foundation

var LC = readLine()!.split(separator: " ").map { Int($0)! }
var L = LC[0], C = LC[1]
var letters = readLine()!.split(separator: " ").map { String($0) }

func solve(_ L: Int, _ C: Int, _ letters: [String]) {
    var res: [String] = []
    var v: Set<String> = ["a", "e", "i", "o", "u"]
    var letters = letters.sorted()
    
    func check(_ candidate: String) -> Bool {
        var count = 0
        for c in candidate {
            if v.contains(String(c)) {
                count += 1
            }
        }
        
        return candidate.count - count > 1 && count > 0 ? true : false
    }
    
    func backtrack(_ i: Int, _ temp: inout [String]) {
        if temp.count == L {
            var candidate = temp.joined()
            if check(candidate) {
                res.append(candidate)
            }
            
            return
        }
        
        if i < C {
            temp.append(letters[i])
            backtrack(i + 1, &temp)
            temp.popLast()
            backtrack(i + 1, &temp)
        }
    }
    
    var temp: [String] = []
    backtrack(0, &temp)
    
    for r in res {
        print(r)
    }
}

solve(L, C, letters)
