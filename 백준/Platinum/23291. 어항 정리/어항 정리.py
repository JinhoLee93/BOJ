from collections import deque

N, K = list(map(int, input().strip().split()))
bowls = deque(list(map(int, input().strip().split())))

def solve(bowls):
    res = 0
    while max(bowls) - min(bowls) > K:
        minimumFish = min(bowls)
        for i in range(N):
            if bowls[i] == minimumFish:
                bowls[i] += 1

        height, length = 1, 1
        merged = [bowls]
        while True:
            if len(merged[0]) - length < height:
                break
            stack = [deque([]) for _ in range(length)]
            for l in range(length - 1, -1, -1):
                for h in range(height):
                    stack[l].append(merged[h].popleft())

            nxtMerged = []
            for h in range(height):
                if merged[h]:
                    nxtMerged.append(merged[h])

            merged = nxtMerged
            for s in stack:
                merged.append(s)

            if height == length:
                height += 1
            elif height > length:
                length += 1

        bowlsToBeAdded = []
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        height = len(merged)
        for h in range(height):
            length = len(merged[h])
            for l in range(length):
                for d in dirs:
                    nxtH, nxtL = h + d[0], l + d[1]
                    if nxtH < 0 or nxtL < 0 or nxtH >= height or nxtL >= len(merged[nxtH]) or \
                        (nxtH, nxtL, h, l) in visited or (h, l, nxtH, nxtL) in visited:
                        continue
                    diff = abs(merged[h][l] - merged[nxtH][nxtL]) // 5
                    if diff > 0:
                        if merged[h][l] > merged[nxtH][nxtL]:
                            bowlsToBeAdded.append((nxtH, nxtL, diff, h, l, -1 * diff))
                        else:
                            bowlsToBeAdded.append((h, l, diff, nxtH, nxtL, -1 * diff))
                        visited.add((nxtH, nxtL, h, l))
                        visited.add((h, l, nxtH, nxtL))

        for b in bowlsToBeAdded:
            aH, aL, aD, sH, sL, sD = b
            merged[aH][aL] += aD
            merged[sH][sL] += sD

        # First division and rotation
        newBowls = deque([])
        length = len(merged[0])
        for l in range(length):
            for h in range(height):
                if len(merged[h]) <= l:
                    continue
                newBowls.append(merged[h][l])

        half = deque([])
        for _ in range(N // 2):
            half.appendleft(newBowls.popleft())
        # Second division and rotation
        newMerged = [newBowls, half]
        secondHalf = [deque([]) for _ in range(2)]
        for h in range(1, -1, -1):
            for l in range(N // 4):
                secondHalf[h].appendleft(newMerged[h].pop())
        for h in range(2):
            newMerged[h].reverse()
        newMerged.reverse()

        for h in range(2):
            secondHalf.append(newMerged[h])

        newMerged = secondHalf
        bowlsToBeAdded = []
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        height = len(newMerged)
        for h in range(height):
            length = len(newMerged[h])
            for l in range(length):
                for d in dirs:
                    nxtH, nxtL = h + d[0], l + d[1]
                    if nxtH < 0 or nxtL < 0 or nxtH >= height or nxtL >= len(newMerged[nxtH]) or \
                            (nxtH, nxtL, h, l) in visited or (h, l, nxtH, nxtL) in visited:
                        continue
                    diff = abs(newMerged[h][l] - newMerged[nxtH][nxtL]) // 5
                    if diff > 0:
                        if newMerged[h][l] > newMerged[nxtH][nxtL]:
                            bowlsToBeAdded.append((nxtH, nxtL, diff, h, l, -1 * diff))
                        else:
                            bowlsToBeAdded.append((h, l, diff, nxtH, nxtL, -1 * diff))
                        visited.add((nxtH, nxtL, h, l))
                        visited.add((h, l, nxtH, nxtL))

        for b in bowlsToBeAdded:
            aH, aL, aD, sH, sL, sD = b
            newMerged[aH][aL] += aD
            newMerged[sH][sL] += sD

        bowls = deque([])
        height = len(newMerged)
        for l in range(N // 4):
            for h in range(height):
                bowls.append(newMerged[h][l])

        res += 1

    print(res)

solve(bowls)