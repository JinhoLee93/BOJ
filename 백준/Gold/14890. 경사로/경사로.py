N, L = list(map(int, input().split(" ")))
board = []

for _ in range(N):
    board.append(list(map(int, input().split(" "))))

def solve():
    res = 0
    visited = set()
    # row-wise path
    for r in range(N):
        complete, left, right, steps, ramps = True, False, False, 1, set()
        for c in range(1, N):
            prv, cur = board[r][c - 1], board[r][c]
            if prv == cur:
                steps += 1

            elif prv == cur + 1: # Should Put Up Left
                if right:
                    complete = False
                    break

                if not left:
                    left = True
                    steps = 1
                else:
                    complete = False
                    break

            elif prv + 1 == cur and not right: # Should Put Up Right
                if left:
                    complete = False
                    break

                if not right:
                    right = True
                else:
                    complete = False
                    break

            elif prv + 1 < cur:
                complete = False
                break

            elif prv > cur + 1:
                complete = False
                break

            if left:
                if steps >= L: # Put a ramp
                    unableToPutRamp = False
                    for leftCol in range(c, c - L, -1):
                        if (r, leftCol) in visited:
                            unableToPutRamp = True
                            break
                        ramps.add((r, leftCol))
                    if unableToPutRamp:
                        complete = False
                        break
                    left = False
                    steps = 0

            if right:
                if steps >= L:
                    unableToPutRamp = False
                    prvCol = c - 1
                    for rightCol in range(prvCol, prvCol - L, -1):
                        if (r, rightCol) in visited:
                            unableToPutRamp = True
                            break
                        ramps.add((r, rightCol))
                    if unableToPutRamp:
                        complete = False
                        break
                    right = False
                    steps = 1

                else:
                    complete = False
                    break

        if complete:
            if right or left:
                continue
            visited = visited.union(ramps)
            res += 1

    visited = set()
    for c in range(N):
        complete, up, down, steps, ramps = True, False, False, 1, set()
        for r in range(1, N):
            prv, cur = board[r - 1][c], board[r][c]
            if prv == cur:
                steps += 1

            elif prv == cur + 1:  # Should Put Up Ramp
                if down:
                    complete = False
                    break

                if not up:
                    up = True
                    steps = 1
                else:
                    complete = False
                    break

            elif prv + 1 == cur and not down:  # Should Put Down Ramp
                if up:
                    complete = False
                    break

                if not down:
                    down = True
                else:
                    complete = False
                    break

            elif prv + 1 < cur:
                complete = False
                break

            elif prv > cur + 1:
                complete = False
                break

            if up:
                if steps >= L:  # Put a ramp
                    unableToPutRamp = False
                    for upRow in range(r, r - L, -1):
                        if (upRow, c) in visited:
                            unableToPutRamp = True
                            break
                        ramps.add((upRow, c))
                    if unableToPutRamp:
                        complete = False
                        break
                    up = False
                    steps = 0

            if down:
                if steps >= L:
                    unableToPutRamp = False
                    prvRow = r - 1
                    for downRow in range(prvRow, prvRow - L, -1):
                        if (downRow, c) in visited:
                            unableToPutRamp = True
                            break
                        ramps.add((downRow, c))
                    if unableToPutRamp:
                        complete = False
                        break
                    down = False
                    steps = 1
                else:
                    complete = False
                    break

        if complete:
            if up or down:
                continue
            visited = visited.union(ramps)
            res += 1

    print(res)

solve()