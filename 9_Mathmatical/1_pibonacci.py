N = int(input())

def solution(N):
    if N == 0:
        return 0
    if N == 1:
        return 1

    return solution(N - 1) + solution(N - 2)

print(solution(N))