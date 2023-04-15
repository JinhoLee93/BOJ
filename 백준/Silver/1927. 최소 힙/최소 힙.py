import sys
import heapq

N = int(input())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if not heap:
            print(0)
            continue
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)