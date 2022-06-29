import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = sorted(map(int, input().split()))
seq = [0] * M
visit = [False] * N


def backtracking(K):
    if K == M:
        for m in range(M):
            print(seq[m], end=' ')
        print()
        return None
    check = 0
    for i in range(N):
        if not visit[i] and check != num[i]:
            seq[K] = num[i]
            visit[i] = True
            check = num[i]
            backtracking(K + 1)
            visit[i] = False


backtracking(0)
