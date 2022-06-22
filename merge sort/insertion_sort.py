def insertion_sort(arr):
    size = len(arr)

    for i in range(1, size):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)

        arr[j + 1] = key

    return arr

arr = [8, 9, 2, 3, 1, 7, 6, 5,]

print(insertion_sort(arr))