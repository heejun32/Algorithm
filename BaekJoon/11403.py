import sys


# dfs 함수 선언
def dfs(start, end, visit):
    stack = []
    stack.append(GRAPH[start])

    while stack:
        temp = stack.pop()
        for i in range(len(temp)):
            if temp[i] == 1 and end == i:
                return True
            if temp[i] == 1 and not visit[i]:
                visit[i] = True
                stack.append(GRAPH[i])
    return False


# 문제 입력 시작
input = sys.stdin.readline
N = int(input())
GRAPH = []
answer = [[0 for _ in range(N)] for _ in range(N)]

for n in range(N):
    GRAPH.append(list(map(int, input().split())))

# dfs 탐색 시작
for start in range(N):
    for end in range(N):
        visit = [False] * N
        if dfs(start, end, visit):
            answer[start][end] = 1

# 결과 출력
for row in range(N):
    for col in range(N):
        print(answer[row][col], end=" ")
    print()
