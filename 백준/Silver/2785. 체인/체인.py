N = int(input())
links = list(map(int, input().split()))
links.sort()
res = 1
for l in links:
    if res + l >= N:
        break
    else:
        res += l
        N -= 1

print(N - 1)