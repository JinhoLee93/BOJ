import sys

N = int(input())
ppl = []
for _ in range(N):
    ppl.append(int(sys.stdin.readline()))
ppl.sort()
res = 0
for i in range(len(ppl)):
    res += abs(ppl[i] - (i + 1))
print(res)
