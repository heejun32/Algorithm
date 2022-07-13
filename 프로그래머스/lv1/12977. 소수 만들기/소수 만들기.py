from itertools import combinations


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    comb_nums = combinations(nums, 3)
    for comb_num in comb_nums:
        if is_prime(sum(comb_num)):
            answer += 1
    return answer
