import sys
input = sys.stdin.readline

N = int(input())
N_lst = sorted(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))


def binary_search(start, end, target):
    while start <= end:
        middle = (start + end) // 2
        if N_lst[middle] == target:
            return True
        elif N_lst[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    return False


for m in M_lst:
    if binary_search(0, N - 1, m):
        print(1)
    else:
        print(0)
