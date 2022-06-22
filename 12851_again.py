from collections import deque
import sys
input = sys.stdin.readline
MAX = 10 ** 5
BORAD = [[-1, 0] for _ in range(MAX + 1)]    # [동생을 찾는 가장 빠른 시간, 경우의 수]

def bfs(N):
    queue = deque()
    queue.append(N)
    BORAD[N][0] = 0
    BORAD[N][1] = 1

    while queue:
        x = queue.popleft()
        
        for dx in [x - 1, x + 1, x * 2]:
            if dx > -1 and dx < MAX + 1:
                if BORAD[dx][0] == -1:               # 처음 방문할 경우
                    BORAD[dx][0] = BORAD[x][0] + 1  # 걸린 시간 저장
                    BORAD[dx][1] = BORAD[x][1]      # 경우의 수 저장
                    queue.append(dx)
                    
                elif BORAD[dx][0] == BORAD[x][0] + 1:   # 처음 방문한게 아니고 가장 빠른 시간의 경우면
                    BORAD[dx][1] += BORAD[x][1]         # 새 경우의 수 더하기

N, K = map(int, input().split())
bfs(N)

print(BORAD[K][0])
print(BORAD[K][1])

# 왜 초기 1차원 배열 값이 -1, 0 인가? 0 -> 0으로 가면 0초, 경우의 수는 1가지
# 노드에 처음 방문한게 아니라면? 이전 경우의 수에 + 1
# https://velog.io/@dhelee/%EB%B0%B1%EC%A4%80-12851%EB%B2%88-%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%884-Python-%EB%84%88%EB%B9%84-%EC%9A%B0%EC%84%A0-%ED%83%90%EC%83%89BFS