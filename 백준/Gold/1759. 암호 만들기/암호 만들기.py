L, C = list(map(int, input().split(" ")))
letters = sorted(input().split(" "))

def solve():
    res = []
    v = ["a", "e", "i", "o", "u"]
    vowels = set(v)

    def check(s):
        count = 0
        for letter in s:
            if letter in vowels:
                count += 1

        return True if len(s) - count > 1 and count > 0 else False

    def backtrack(i, temp):
        if len(temp) == L:
            t = "".join(temp)
            if check(t):
                res.append(t)

            return

        if i < C:
            temp.append(letters[i])
            backtrack(i + 1, temp)
            temp.pop()
            backtrack(i + 1, temp)

    backtrack(0, [])

    for r in res:
        print(r)

solve()