from collections import deque

def bfs(r, c):
    q = deque([(r, c)])
    count = 0
    v = set()
    while q:
        cr, cc = q.popleft()
        for d in dirs:
            nr, nc = cr + d[0], cc + d[1]
            if 0 <= nr < 5 and 0 <= nc < 5 and (nr, nc) not in v and visited[nr][nc] == 1:
                v.add((nr, nc))
                q.append((nr, nc))
                count += 1

    return count == 7

def checkbfs():
    for r in range(5):
        for c in range(5):
            if visited[r][c] == 1:

                return bfs(r, c)

def backtrack(i, count, scount):
    global res
    if count == 7:
        if scount >= 4:
            if checkbfs():
                res += 1

        return

    if i < 25:
        visited[i//5][i%5] = 1
        backtrack(i + 1, count + 1, scount + int(board[i//5][i%5] == "S"))
        visited[i//5][i%5] = 0
        backtrack(i + 1, count, scount)

board = []
for _ in range(5):
    b = [str(x) for x in input()]
    board.append(b)
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = 0
visited = [[0] * 5 for _ in range(5)]
backtrack(0, 0, 0)
print(res)