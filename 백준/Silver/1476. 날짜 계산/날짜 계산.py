import sys

'''
Time Complexity is O(E, S, M의 최소공배수)
Space Complexity is O(1)
'''


E, S, M = map(int, sys.stdin.readline().split())


def solution(E: int, S: int, M: int) -> int:
    year = 1
    while(1):
        if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0:
            return year
        year += 1


print(solution(E, S, M))
