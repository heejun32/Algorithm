# tim sort 참고, flake8 코드 스타일 적용
import time


def insertion_sort(arr, start, end):  # in-place / stable
    for i in range(start + 1, end):
        key = arr[i]
        j = i - 1

        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, first, midpoint, last):
    merge_arr = []
    start = first
    mid = midpoint

    while start < midpoint and mid < last:
        if arr[start] < arr[mid]:
            merge_arr.append(arr[start])
            start += 1
        else:
            merge_arr.append(arr[mid])
            mid += 1

    while start < midpoint:
        merge_arr.append(arr[start])
        start += 1

    while mid < last:
        merge_arr.append(arr[mid])
        mid += 1

    for i in range(first, last):
        arr[i] = merge_arr[i - first]


def merge_sort(arr, first, last):
    if last - first <= 32:
        insertion_sort(arr, first, last)
    else:
        midpoint = (first + last) // 2
        merge_sort(arr, first, midpoint)
        merge_sort(arr, midpoint, last)
        merge(arr, first, midpoint, last)


# arr = [i for i in range(1000000, 0, - 1)]
arr = [i for i in range(100_000, 0, -1)]
start = time.time()
merge_sort(arr, 0, len(arr))
end = time.time()

print(arr)
print(end - start)
