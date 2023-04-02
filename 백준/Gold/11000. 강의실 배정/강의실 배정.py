import sys

N = int(input())
times = []
for _ in range(N):
    times.append(list(map(int, sys.stdin.readline().split(" "))))

def solve():
    room = 0
    start, end = [], []
    for time in times:
        start.append(time[0])
        end.append(time[1])

    start.sort()
    end.sort()

    num = len(start)

    i, j, curRoom = 0, 0, 0
    while i < num and j < num:
        s, e = start[i], end[j]
        if s < e:
            curRoom += 1
            i += 1
        else:
            if curRoom > 0:
                curRoom -= 1
            j += 1
        room = max(room, curRoom)

    print(room)

solve()