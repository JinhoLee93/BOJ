import sys

N = int(input())
lines = []
for _ in range(N):
    lines.append(list(map(int, sys.stdin.readline().split(" "))))

def solve():
    res = 0
    for line in lines:
        if line[0] > line[1]:
            line[0], line[1] = line[1], line[0]

    lines.sort(key= lambda x:x[0])

    leftMost, rightMost = lines[0][0], lines[0][1]
    for i in range(len(lines) - 1):
        cur, nxt = lines[i], lines[i + 1]
        curStart, curEnd = cur[0], cur[1]
        nxtStart, nxtEnd = nxt[0], nxt[1]
        rightMost = max(rightMost, curEnd)
        if nxtStart <= rightMost:
            leftMost = min(leftMost, curStart)
        else:
            res += rightMost - leftMost
            leftMost = nxtStart
            rightMost = nxtEnd

    leftMost = min(leftMost, lines[-1][0])
    rightMost = max(rightMost, lines[-1][1])
    res += rightMost - leftMost
    print(res)

solve()