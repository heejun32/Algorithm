def insertion_sort(arr, start, end):
    for i in range(start, end):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# insertion sort는 탐색 범위 전 범위가 정렬 되어 있다고 가정 그래서 인덱스를 보통 1부터 시작한다.
# 그러나 merge sort의 경우 merge하는 과정에서 왼쪽 sub list 와 오른쪽 sub list 를 합치기에
# insertion sort가 받는 첫번째 배열이 보통의 인덱스 1번째 기준이 된다.
# Ex 7 8 9 10 11 5 6, 여기서 start + 1을 하면 5는 정렬을 건너 뛰고 6부터 확인하기 때문에 5가 정렬이 되지 않는다.
# 따라서 insertion sort가 받는 배열의 시작인 인덱스 0이 기존 insertion sort 배열의 시작점인 인덱스 1의 역할을 한다.


def merge(arr, first, midpoint, last):
    merge_arr = []
    mid = midpoint

    while first < midpoint and mid < last:
        if arr[first] < arr[mid]:
            merge_arr.append(arr[first])
            first += 1
        else:
            merge_arr.append(arr[mid])
            mid += 1
    if first == midpoint:
        merge_arr += arr[mid: last]
    else:
        merge_arr += arr[first: midpoint]
    return merge_arr

def merge_sort(arr, first, last):
    if last - first <= 6:
        insertion_sort(arr, first, last)
    else:
        midpoint = (first + last) // 2
        merge_sort(arr, first, midpoint)
        merge_sort(arr, midpoint, last)
        merge(arr, first, midpoint, last)
    return arr

arr = [i for i in range(10, 0, - 1)]
# arr = [1, 0]

print(merge_sort(arr, 0, len(arr)))