import sys
import heapq

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    k = int(input())
    visited = [False] * 1_000_000
    min_Q = []
    max_Q = []
    
    for i in range(k):
        operation = list(input().split())
        
        if operation[0] == 'I':
            value = int(operation[-1])
            heapq.heappush(min_Q, (value, i))
            heapq.heappush(max_Q, (-1 * value, i))
            visited[i] = True
        elif operation[-1] == '1':
            while max_Q and not visited[max_Q[0][1]]:
                heapq.heappop(max_Q)
            if max_Q:
                visited[max_Q[0][1]] = False
                heapq.heappop(max_Q)
        else:
            while min_Q and not visited[min_Q[0][1]]:
                heapq.heappop(min_Q)
            if min_Q:
                visited[min_Q[0][1]] = False
                heapq.heappop(min_Q)
    
    while max_Q and not visited[max_Q[0][1]]:
        heapq.heappop(max_Q)
    while min_Q and not visited[min_Q[0][1]]:
        heapq.heappop(min_Q)

    if min_Q and max_Q:
        print(f'{-1 * max_Q[0][0]} {min_Q[0][0]}')
    else:
        print('EMPTY')