from collections import deque

N, K = list(map(int, input().strip().split()))
b = deque(list(map(int, input().strip().split())))
r = deque([False] * N)
p, d = 0, 0
def s1():
    b.rotate(1)
    r.rotate(1)

def s2():
    global p, d
    r[-1] = False
    for i in range(len(r) - 2, -1, -1):
        if r[i]:
            if b[i + 1] > 0 and not r[i + 1]:
                if i + 1 == N - 1:
                    r[i] = False
                else:
                    r[i], r[i + 1] = False, True
                b[i + 1] -= 1
                if b[i + 1] == 0:
                    d += 1
                    if d == K:
                        print(f"{p}")
                        exit(0)

def s3():
    global p, d
    if b[0] > 0:
        r[0] = True
        b[0] -= 1
        if b[0] == 0:
            d += 1
            if d == K:
                print(f"{p}")
                exit(0)

while True:
    p += 1
    s1()
    s2()
    s3()