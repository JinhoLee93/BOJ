var N = Int(readLine()!)!
var times: [[Int]] = []
for _ in 0..<N {
    var time = readLine()!.split(separator: " ").map { Int($0)! }
    times.append(time)
}

func solve(_ N: Int, _ times: [[Int]]) {
    var room = 0
    var start: [Int] = [], end: [Int] = []
    for time in times {
        start.append(time[0])
        end.append(time[1])
    }
    
    start.sort()
    end.sort()
    
    var i = 0, j = 0, curRoom = 0
    while i < start.count && j < end.count {
        var s = start[i], e = end[j]
        if s < e {
            curRoom += 1
            i += 1
        } else {
            if curRoom > 0 {
                curRoom -= 1
            }
            j += 1
        }
        room = max(room, curRoom)
    }
    
    print(room)
}

solve(N, times)
