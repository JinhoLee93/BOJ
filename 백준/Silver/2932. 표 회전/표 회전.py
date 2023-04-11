N, K = list(map(int,input().strip().split()))

rotations = []
for _ in range(K):
    X, R, C = list(map(int, input().strip().split()))
    curR = ((X - 1) // N)
    curC = ((X - 1) % N)
    rotation = [X, curR, curC, R - 1, C - 1]
    rotations.append(rotation)

def move(c, t):
    moved = 0
    if t > c:
        moved += t - c
    elif t < c:
        moved += N - abs(t - c)

    return moved

for k in range(K):
    res = 0
    cv, cr, cc, tr, tc = rotations[k]
    col_moved = move(cc, tc)
    row_moved = move(cr, tr)
    res += col_moved + row_moved

    for nxtK in range(k + 1, K):
        if rotations[nxtK][0] == cv:
            rotations[nxtK][1] = tr
            rotations[nxtK][2] = tc
        else:
            if rotations[nxtK][1] == cr:
                rotations[nxtK][2] += col_moved
                if rotations[nxtK][2] >= N:
                    rotations[nxtK][2] %= N

            if rotations[nxtK][2] == tc:
                rotations[nxtK][1] += row_moved
                if rotations[nxtK][1] >= N:
                    rotations[nxtK][1] %= N

    print(res)