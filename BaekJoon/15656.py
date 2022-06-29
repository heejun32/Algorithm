import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
seq = [0] * N


def backtracking(K):
    if K == M:
        for m in range(M):
            print(seq[m], end=' ')
        print()
        return None
    for i in range(N):
        seq[K] = nums[i]
        backtracking(K + 1)


backtracking(0)
