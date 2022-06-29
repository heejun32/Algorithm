from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline


def bisect(arr, num):
    left_index = bisect_left(arr, num)
    right_index = bisect_right(arr, num)
    return str(right_index - left_index)


N = int(input())
N_lst = sorted(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))
answer = []

for m in M_lst:
    answer.append(bisect(N_lst, m))

print(' '.join(answer))
