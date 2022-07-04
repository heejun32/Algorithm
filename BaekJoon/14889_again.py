import sys


def dfs(idx, depth):
    global answer
    if depth == N // 2:
        start_sum = 0
        link_sum = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start_sum += S[i][j]
                elif not visited[i] and not visited[j]:
                    link_sum += S[i][j]
        answer = min(answer, abs(start_sum - link_sum))
        return


    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(idx + 1, depth + 1)
            visited[i] = False


inputs = sys.stdin.readline
N = int(inputs())
S = [list(map(int, inputs().split())) for _ in range(N)]
visited = [False] * N
answer = sys.maxsize

dfs(0, 0)
print(answer)
