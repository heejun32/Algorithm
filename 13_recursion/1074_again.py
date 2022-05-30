import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())


# 재귀 풀이
def recursion(N, r, c):
    if N == 0:
        return 0

    return 2 * (r % 2) + (c % 2) + 4 * recursion(N - 1, r // 2, c // 2)


print(recursion(N, r, c))

# 분할 정복 풀이
answer = 0

while N != 0:
    # 4 등분으로 나누자
    N -= 1

    # 1 사분면
    if r < 2 ** N and c < 2 ** N:
        answer += (2 ** N) * (2 ** N) * 0

    # 2 사분면
    if r < 2 ** N and c >= 2 ** N:
        answer += (2 ** N) * (2 ** N) * 1
        c -= (2 ** N)

    # 3 사분면
    if r >= 2 ** N and c < 2 ** N:
        answer += (2 ** N) * (2 ** N) * 2
        r -= (2 ** N)

    # 4 사분면
    if r >= 2 ** N and c >= 2 ** N:
        answer += (2 ** N) * (2 ** N) * 3
        r -= (2 ** N)
        c -= (2 ** N)

print(answer)
# 참고 사이트: https://ggasoon2.tistory.com/11
