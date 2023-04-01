N = int(input())

def solve():
    board = [[0 for _ in range(N)] for _ in range(N)]
    res = 0
    leftDiag = set()
    col = set()
    rightDiag = set()

    def backtrack(r):
        nonlocal res
        if r == N:
            res += 1

            return

        for c in range(N):
            left, right = r + c, r - c
            if left in leftDiag or right in rightDiag or c in col:
                continue
            board[r][c] = 1
            leftDiag.add(left)
            col.add(c)
            rightDiag.add(right)
            backtrack(r + 1)
            leftDiag.remove(left)
            col.remove(c)
            rightDiag.remove(right)
            board[r][c] = 0

    backtrack(0)

    print(res)

solve()