N = int(input().strip())

i = 1
ppl = []
for _ in range(N):
    ppl.append(i)
    i += 1

pos = 0
stage = 1
while len(ppl) > 1:
    target = stage ** 3
    numOfPpl = len(ppl)
    toBeRemoved = ((pos) + (target - 1)) % numOfPpl
    ppl.pop(toBeRemoved)
    pos = toBeRemoved
    stage += 1
    
print(ppl[0])             