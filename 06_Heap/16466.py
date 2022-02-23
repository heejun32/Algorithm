import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = list(map(int, input().split()))

heapq.heapify(heap)

for i in range(1, 2 ** 31):
    if N > 0:
        if i < heap[0]:
            print(i)
            break
        else:
            heapq.heappop(heap)
            N -= 1