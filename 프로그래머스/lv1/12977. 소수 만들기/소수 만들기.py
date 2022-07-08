from itertools import combinations


def isprime(num : int) -> bool:
    # 1이면 반환
    if num == 1:
        return False
    # 1이 아니면 탐색 시작
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    combs = list(combinations(nums, 3))
    for comb in combs:
        if isprime(sum(comb)):
            answer += 1
    return answer

