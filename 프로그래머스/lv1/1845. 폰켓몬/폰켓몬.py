from collections import Counter


def solution(nums):
    answer = 0
    n = len(nums) // 2
    counter = Counter(nums)
    
    if len(counter) >= n:
        answer = n
    else:
        answer = len(counter)
    return answer