from typing import List
import sys

'''
Time Complexity is O(NM). N은 채널의 범위, M은 탐색하는 채널의 자릿수 
Space Complexity is O(1)
'''


def solution() -> int:
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    break_nums = list(sys.stdin.readline().split())
    answer = abs(100 - N)

    for channel in range(1_000_001):
        channel = str(channel)

        # 버튼으로 검색할 수 없는 채널이라면 탐색 x
        for i in range(len(channel)):
            if channel[i] in break_nums:
                break

            # 버튼으로 해당 채널을 검색할 수 있다면
            elif i == len(channel) - 1:
                answer = min(answer, abs(N - int(channel)) +len(channel))

    return answer

print(solution())
