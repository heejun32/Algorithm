from collections import deque
import sys
input = sys.stdin.readline


# 함수 선언
def bfs(F, S, G, U, D):
    queue = deque()
    queue.append(S)
    visit[S] = 1

    while queue:
        now = queue.popleft()
        if now == G:
            return visit[G] - 1
        if now + U <= F and not visit[now + U]:
            visit[now + U] = visit[now] + 1
            queue.append(now + U)
        if now - D >= 1 and not visit[now - D]:
            visit[now - D] = visit[now] + 1
            queue.append(now - D)

    return 'use the stairs'


# 입력값 처리
F, S, G, U, D = map(int, input().split())
visit = [0] * (F + 1)

# bfs 탐색 시작
print(bfs(F, S, G, U, D))
