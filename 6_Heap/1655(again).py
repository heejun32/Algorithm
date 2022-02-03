import sys
import heapq
input = sys.stdin.readline

# 작은 값들 중 제일 큰 값 < 큰 값들 중 제일 작은 값 = 중간 값

N = int(input())
left_heap = []
right_heap = []
for _ in range(N):
    number = int(input())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -1 * number)
    else:
        heapq.heappush(right_heap, number)
    if right_heap and -1 * left_heap[0] > right_heap[0]:
        left = -1 * heapq.heappop(left_heap)
        right = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -1 * right)
        heapq.heappush(right_heap, left)
    print(-1 * left_heap[0])
