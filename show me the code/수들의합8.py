import sys


def dfs(idx, total_A, total_B):
    global answer

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            if A[i] == B[i]:
                answer += 1
            if total_A + A[i] == total_B + B[i]:
                answer += 1

            dfs(i + 1, total_A + A[i], total_B + B[i])
            visited[i] = False
            dfs(i + 1, A[i], B[i])
            visited[i] = True



N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
visited = [False] * N
answer = 0
dfs(0, 0, 0)
print(answer)