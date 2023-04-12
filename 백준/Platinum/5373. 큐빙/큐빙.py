def solve():
    U = [["w"] * 3 for _ in range(3)]
    B = [["o"] * 3 for _ in range(3)]
    F = [["r"] * 3 for _ in range(3)]
    D = [["y"] * 3 for _ in range(3)]
    L = [["g"] * 3 for _ in range(3)]
    R = [["b"] * 3 for _ in range(3)]

    def rotate90(dir, side):
        rotated = [[] for _ in range(3)]
        if dir == "+":
            for r in range(2, -1, -1):
                for c in range(3):
                    rotated[c].append(side[r][c])
        else:
            for r in range(3):
                for c in range(2, -1, -1):
                    rotated[c].append(side[r][c])
            rotated[0], rotated[2] = rotated[2], rotated[0]

        return rotated

    def rotateF(dir, F, U, L, R, D):
        F = rotate90(dir, F)
        u, l, r, d = [], [], [], []
        candidates = ["u", "l", "r", "d"]
        for c in candidates:
            for idx in range(3):
                if c == "u":
                    u.append(U[2][idx])
                elif c == "l":
                    l.append(L[2][idx])
                elif c == "r":
                    r.append(R[2][idx])
                elif c == "d":
                    d.append(D[0][idx])

        toBeChanged = ["U", "L", "R", "D"]
        for s in toBeChanged:
            for idx in range(3):
                if s == "U":
                    if dir == "+":
                        U[2][idx] = l[idx]
                    else:
                        U[2][idx] = r[idx]
                elif s == "L":
                    if dir == "+":
                        L[2][2 - idx] = d[idx]
                    else:
                        L[2][idx] = u[idx]
                elif s == "R":
                    if dir == "+":
                        R[2][idx] = u[idx]
                    else:
                        R[2][2 - idx] = d[idx]
                elif s == "D":
                    if dir == "+":
                        D[0][2 - idx] = r[idx]
                    else:
                        D[0][2 - idx] = l[idx]

        return F, U, L, R, D

    def rotateB(dir, B, L, U, R, D):
        B = rotate90(dir, B)
        l, u, r, d = [], [], [], []
        candidates = ["l", "u", "r", "d"]
        for c in candidates:
            for idx in range(3):
                if c == "l":
                    l.append(L[0][idx])
                elif c == "u":
                    u.append(U[0][idx])
                elif c == "r":
                    r.append(R[0][idx])
                elif c == "d":
                    d.append(D[2][idx])

        toBeChanged = ["L", "U", "R", "D"]
        for s in toBeChanged:
            for idx in range(3):
                if s == "L":
                    if dir == "+":
                        L[0][idx] = u[idx]
                    else:
                        L[0][2 - idx] = d[idx]
                elif s == "U":
                    if dir == "+":
                        U[0][idx] = r[idx]
                    else:
                        U[0][idx] = l[idx]
                elif s == "R":
                    if dir == "+":
                        R[0][2 - idx] = d[idx]
                    else:
                        R[0][idx] = u[idx]
                elif s == "D":
                    if dir == "+":
                        D[2][2 - idx] = l[idx]
                    else:
                        D[2][2 - idx] = r[idx]

        return B, L, U, R, D

    def rotateD(dir, D, L, F, R, B):
        D = rotate90(dir, D)
        l, f, r, b = [], [], [], []
        candidates = ["l", "f", "r", "b"]
        for c in candidates:
            for idx in range(3):
                if c == "l":
                    l.append(L[idx][0])
                elif c == "f":
                    f.append(F[2][idx])
                elif c == "r":
                    r.append(R[idx][2])
                elif c == "b":
                    b.append(B[0][idx])

        toBeChanged = ["L", "F", "R", "B"]
        for s in toBeChanged:
            for idx in range(3):
                if s == "L":
                    if dir == "+":
                        L[2 - idx][0] = b[idx]
                    else:
                        L[idx][0] = f[idx]
                elif s == "F":
                    if dir == "+":
                        F[2][idx] = l[idx]
                    else:
                        F[2][2 - idx] = r[idx]
                elif s == "R":
                    if dir == "+":
                        R[2 - idx][2] = f[idx]
                    else:
                        R[idx][2] = b[idx]
                elif s == "B":
                    if dir == "+":
                        B[0][idx] = r[idx]
                    else:
                        B[0][2 - idx] = l[idx]

        return D, L, F, R, B

    def rotateU(dir, U, L, R, F, B):
        U = rotate90(dir, U)
        l, r, f, b = [], [], [], []
        candidates = ["l", "r", "f", "b"]
        for c in candidates:
            for idx in range(3):
                if c == "l":
                    l.append(L[idx][2])
                elif c == "r":
                    r.append(R[idx][0])
                elif c == "f":
                    f.append(F[0][idx])
                elif c == "b":
                    b.append(B[2][idx])

        toBeChanged = ["L", "R", "F", "B"]
        for s in toBeChanged:
            for idx in range(3):
                if s == "L":
                    if dir == "+":
                        L[idx][2] = f[idx]
                    else:
                        L[2 - idx][2] = b[idx]
                elif s == "R":
                    if dir == "+":
                        R[idx][0] = b[idx]
                    else:
                        R[2 - idx][0] = f[idx]
                elif s == "F":
                    if dir == "+":
                        F[0][2 - idx] = r[idx]
                    else:
                        F[0][idx] = l[idx]
                elif s == "B":
                    if dir == "+":
                        B[2][2 - idx] = l[idx]
                    else:
                        B[2][idx] = r[idx]

        return U, L, R, F, B

    def rotateL(dir, L, B, U, F, D):
        L = rotate90(dir, L)
        b, u, f, d = [], [], [], []
        candidates = ["b", "u", "f", "d"]
        for c in candidates:
            for idx in range(3):
                if c == "b":
                    b.append(B[idx][0])
                elif c =="u":
                    u.append(U[idx][0])
                elif c == "f":
                    f.append(F[idx][0])
                elif c == "d":
                    d.append(D[idx][0])

        toBeChanged = ["B", "U", "F", "D"]
        for s in toBeChanged:
            for idx in range(3):
                if s == "B":
                    if dir == "+":
                        B[idx][0] = d[idx]
                    else:
                        B[idx][0] = u[idx]
                elif s == "U":
                    if dir == "+":
                        U[idx][0] = b[idx]
                    else:
                        U[idx][0] = f[idx]
                elif s == "F":
                    if dir == "+":
                        F[idx][0] = u[idx]
                    else:
                        F[idx][0] = d[idx]
                elif s == "D":
                    if dir == "+":
                        D[idx][0] = f[idx]
                    else:
                        D[idx][0] = b[idx]

        return L, B, U, F, D

    def rotateR(dir, R, B, U, F, D):
        R = rotate90(dir, R)
        b, u, f, d = [], [], [], []
        candidates = ["b", "u", "f", "d"]
        for c in candidates:
            for idx in range(3):
                if c == "b":
                    b.append(B[idx][2])
                elif c == "u":
                    u.append(U[idx][2])
                elif c == "f":
                    f.append(F[idx][2])
                elif c == "d":
                    d.append(D[idx][2])

        toBeChanged = ["B", "U", "F", "D"]
        for s in toBeChanged:
            for idx in range(3):
                if s == "B":
                    if dir == "+":
                        B[idx][2] = u[idx]
                    else:
                        B[idx][2] = d[idx]
                elif s == "U":
                    if dir == "+":
                        U[idx][2] = f[idx]
                    else:
                        U[idx][2] = b[idx]
                elif s == "F":
                    if dir == "+":
                        F[idx][2] = d[idx]
                    else:
                        F[idx][2] = u[idx]
                elif s == "D":
                    if dir == "+":
                        D[idx][2] = b[idx]
                    else:
                        D[idx][2] = f[idx]

        return R, B, U, F, D

    for i in range(rotations):
        cur = directions[i]
        side, dir = cur[0], cur[1]
        if side == "F":
            F, U, L, R, D = rotateF(dir, F, U, L, R, D)
        elif side == "B":
            B, L, U, R, D = rotateB(dir, B, L, U, R, D)
        elif side == "D":
            D, L, F, R, B = rotateD(dir, D, L, F, R, B)
        elif side == "U":
            U, L, R, F, B = rotateU(dir, U, L, R, F, B)
        elif side == "L":
            L, B, U, F, D = rotateL(dir, L, B, U, F, D)
        elif side == "R":
            R, B, U, F, D = rotateR(dir, R, B, U, F, D)

    for r in range(3):
        print("".join(U[r]))
T = int(input().strip())

for _ in range(T):
    rotations = int(input().strip())
    directions = list(input().strip().split())
    solve()