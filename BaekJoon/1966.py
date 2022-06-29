from collections import deque
import sys

input = sys.stdin.readline
T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    order = deque([i for i in range(N)])
    priority = deque(map(int, input().split()))
    count = 0

    while priority:
        if priority[0] < max(priority):
            priority.append(priority.popleft())
            order.append(order.popleft())
        else:
            priority.popleft()
            count += 1
            if M == order.popleft():
                print(count)
                break
