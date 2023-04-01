N = int(input())
eggs = []
for _ in range(N):
    eggs.append(list(map(int, input().split(" ")))) # durability, weight

def solve():
    res = 0
    def backtrack(i):
        nonlocal res
        if i == N:
            curRes = 0
            for egg in eggs:
                if egg[0] <= 0:
                    curRes += 1
            res = max(res, curRes)

            return

        if eggs[i][0] <= 0:
            backtrack(i + 1)
        else:
            empty = True
            for j in range(N):
                if i != j and eggs[j][0] > 0:
                    empty = False
                    eggs[j][0] -= eggs[i][1]
                    eggs[i][0] -= eggs[j][1]
                    backtrack(i + 1)
                    eggs[j][0] += eggs[i][1]
                    eggs[i][0] += eggs[j][1]

            if empty:
                backtrack(N)

    backtrack(0)
    print(res)
solve()