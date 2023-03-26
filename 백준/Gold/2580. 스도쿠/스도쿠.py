import sys
import copy
from collections import deque
sys.setrecursionlimit(10**6)

board = []
for _ in range(9):
    board.append(list(map(int, input().split(" "))))

def solve(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    squares = [set() for _ in range(9)]
    zeros = deque()

    for r in range(9):
        for c in range(9):
            if board[r][c] != 0:
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sqIdx = (r // 3) * 3 + (c // 3)
                squares[sqIdx].add(board[r][c])
            else:
                zeros.append((r, c))

    def backtrack():
        if not zeros:
            for row in range(9):
                print(" ".join(str(n) for n in board[row]))
            exit(0)

            return

        r, c = zeros.popleft()
        sqIdx = (r // 3 * 3) + c // 3
        for num in range(1, 10):
            if num not in rows[r] and num not in cols[c] and num not in squares[sqIdx]:
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                squares[sqIdx].add(num)
                backtrack()
                board[r][c] = 0
                rows[r].remove(num)
                cols[c].remove(num)
                squares[sqIdx].remove(num)
        zeros.appendleft((r, c))

    backtrack()

solve(board)
