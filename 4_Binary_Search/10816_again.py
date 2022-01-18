import sys

def binary_search(key, arr):
    start = 0
    end = len(arr) - 1  # 범위 주의1!!!

    while start <= end: # 범위 주의2!!!
        mid = (start + end) // 2

        if key == arr[mid]:
            return True
        if key > arr[mid]:
            start = mid + 1
        if key < arr[mid]:
            end = mid - 1

    return False

    # 조건 충족하면 True
    # 아니면 False

input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
sorted_M_list = sorted(M_list)

dict = {}
for n in N_list:
    if binary_search(n, sorted_M_list):
        dict[n] = dict.get(n, 0) + 1
    else:
        dict[n] = 0

for m in M_list:
    if m in dict.keys():
        print(f"{dict[m]} ", end="")
    else:
        print(0, end=" ")

