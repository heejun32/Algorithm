import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = [0] * N


def backtracking(K):
    if K == M:
        for i in range(M):
            print(seq[i], end=' ')
        print()
        return None
    for i in range(1, N + 1):
        if K == 0:
            seq[K] = i
            backtracking(K + 1)
        elif seq[K - 1] <= i:
            seq[K] = i
            backtracking(K + 1)


backtracking(0)
