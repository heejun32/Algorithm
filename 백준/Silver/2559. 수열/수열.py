import sys


def solution(n: int, k: int, nums) -> int:
    max_temp = float('-inf')
    current_temp = 0
    left = 0
    for right in range(n):
        current_temp += nums[right]
        if right - left + 1 < k:
            continue
        # 최대 온도 비교
        max_temp = max(max_temp, current_temp)
        # 윈도우 사이즈 조절
        current_temp -= nums[left]
        left += 1

    return max_temp


n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
# print(n, k, nums)
print(solution(n, k, nums))
