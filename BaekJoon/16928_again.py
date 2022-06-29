from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque([1])
    visit[1] = True
    while queue:
        now = queue.popleft()
        for dice in range(1, 7):
            new_move = now + dice
            if 0 < new_move <= 100 and not visit[new_move]:
                if new_move in ladder.keys():
                    new_move = ladder[new_move]
                if new_move in snake.keys():
                    new_move = snake[new_move]
                # 뱀과 사다리에 전부 없는 수면
                if not visit[new_move]:
                    queue.append(new_move)
                    visit[new_move] = True
                    board[new_move] = board[now] + 1
    return None


N, M = map(int, input().split())
# 게임 보드는 자연수 1부터 시작, 인덱스 접근을 쉽게하기 위해 배열을 1개씩 늘려 만듦.
board = [0] * 101
visit = [False] * 101

ladder = dict()
snake = dict()
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

# bfs 탐색 시작
bfs()

# 정답 출력
print(board[100])
