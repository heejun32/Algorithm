# flake8 코드 스타일이 적용되어 있습니다.
from collections import deque
import sys
input = sys.stdin.readline
queue = deque()


# bfs 함수
def bfs(V, E, R, D, O):
    V[R] = 1            # 방문 확인
    D[R] = 0            # 깊이 설정
    O[R] = 1
    depth = 0
    order = 1
    queue.append(E[R])

    while queue:
        depth += 1

        for _ in range(len(queue)):
            u = queue.popleft()
            u.sort()  # 오름차순 방문 설정
            for edge in u:
                if V[edge] == 0:
                    order += 1
                    V[edge] = 1
                    D[edge] = depth
                    O[edge] = order
                    queue.append(E[edge])


# 입력값 처리
N, M, R = map(int, input().split())
E = [[] for _ in range(N + 1)]       # 간선 정보
V = [0 for _ in range(N + 1)]        # 방문 정보
D = [-1 for _ in range(N + 1)]       # 깊이 정보
O = [0 for _ in range(N + 1)]        # 순서 정보

for i in range(1, M + 1):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

# bfs 탐색 시작
bfs(V, E, R, D, O)

# 정답 출력
answer = 0
for i in range(1, N + 1):
    answer += D[i] * O[i]
print(answer)
