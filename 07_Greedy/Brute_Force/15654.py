import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
visit = [False] * N
answer = [0] * M


def backtracking(K):
    if K == M:
        for i in range(M):
            print(answer[i], end=' ')
        print()
        return None
    for i in range(N):
        if not visit[i]:
            answer[K] = seq[i]
            visit[i] = True
            backtracking(K + 1)
            visit[i] = False


backtracking(0)
