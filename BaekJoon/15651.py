import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visit = [False for _ in range(N + 1)]
seq = [0] * 7


def backtracking(K):
    if K == M:
        for i in range(M):
            print(seq[i], end=' ')
        print()
        return None
    for i in range(1, N + 1):
        if not visit[i]:
            seq[K] = i
            backtracking(K + 1)


backtracking(0)