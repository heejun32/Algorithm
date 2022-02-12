N = int(input())
N_arr = sorted(list(map(int, input().split())))

M = int(input())
M_arr = list(map(int, input().split()))

def binary_search(number, N_arr, start, end):
    if start > end:
        return 0
    middle = (start + end) // 2

    if N_arr[middle] == number:
        return 1

    if N_arr[middle] > number:
        return binary_search(number, N_arr, start, middle-1)
    else:
        return binary_search(number, N_arr, middle + 1, end)

for number in M_arr:
    start = 0
    end = len(N_arr) - 1
    print(binary_search(number, N_arr, start, end))