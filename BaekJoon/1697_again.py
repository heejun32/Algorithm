from collections import deque
import sys
input = sys.stdin.readline
MAX = 10 ** 5
BORAD = [0] * (MAX + 1)

def bfs(N, M):
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()
        
        if x == M:
            break

        for dx in (x + 1, x - 1, x * 2):
            if dx > -1 and dx < MAX + 1 and not BORAD[dx]:
                BORAD[dx] = BORAD[x] + 1
                queue.append(dx)
    
    answer = BORAD[x]
    return answer

N, M = map(int, input().split())
answer = bfs(N, M)
print(answer)