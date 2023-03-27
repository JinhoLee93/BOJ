import sys

N = int(input())
rooms = []
students = list(map(int, input().split(" ")))
for i in range(len(students)):
    rooms.append(students[i])
main, sub = list(map(int, input().split(" ")))

def solve():
    total = 0
    for room in rooms:
        r = room - main
        if r < 0:
            r = 0
        if r % sub == 0:
            total += 1 + (r // sub)
        else:
            total += 1 + (r // sub) + 1

    return total

print(solve())