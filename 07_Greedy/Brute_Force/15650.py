import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visit = [False for _ in range(N + 1)]
seq = [0] * 8


def backtracking(K):
    if K == M:
        for i in range(M):
            print(seq[i], end=' ')
        print()
        return None
    for i in range(seq[K - 1] + 1, N + 1):
        if not visit[i]:
            seq[K] = i
            visit[i] = True
            backtracking(K + 1)
            visit[i] = False


backtracking(0)
