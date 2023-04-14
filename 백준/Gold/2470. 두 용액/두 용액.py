N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()
minimum = float("inf")
res = []
i, j = 0, N - 1
while i < j:
    mixed = liquid[i] + liquid[j]
    if mixed == 0:
        res = [liquid[i], liquid[j]]
        break
    elif mixed > 0:
        if abs(mixed) < minimum:
            minimum = abs(mixed)
            res = [liquid[i], liquid[j]]
        j -= 1
    else:
        if abs(mixed) < minimum:
            minimum = abs(mixed)
            res = [liquid[i], liquid[j]]
        i += 1

print(res[0], res[1])