from collections import deque
import sys
input = sys.stdin.readline
MAX = 10 ** 5
BORAD = [[0, 0]] * (MAX + 1)

def bfs(N, K):
    queue = deque()
    queue.append(N)
    sec = 0
    ways = 0
    while queue:
        x = queue.popleft()
        
        if x == K:
            break

        for dx in (x + 1, x - 1, x * 2):
            if dx > -1 and dx < MAX + 1 and not BORAD[dx]:
                BORAD[dx] = BORAD[x] + 1
                queue.append(dx)
    
    answers = BORAD[x]
    return answers

N, K = map(int, input().split())
answers = bfs(N, K)

# answer을 리스트로 받아온 상태
for answer in answers:
    print(answer)