from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for num in range(1, N + 1):
    queue.append(num)

while queue:
    last_num = queue.popleft()

    if not queue:
        break

    queue.append(queue.popleft())

print(last_num)