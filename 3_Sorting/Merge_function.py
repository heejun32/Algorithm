arr1 = [1, 3, 4, 5, 5, 6, 7, 45, 54, 123, 231, 321, 432, 456, 456, 632, 874]
arr2 = [1, 1, 2, 4, 5, 6, 25, 43, 123, 234, 234, 321, 423, 432, 523, 532]
merge_arr = []
i = 0
j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        merge_arr.append(arr1[i])
        i += 1
    else:
        merge_arr.append(arr2[j])
        j += 1

if i == len(arr1):
    merge_arr += arr2[j:]
else:
    merge_arr += arr1[i:]

print(arr1)
print(arr2)
print(merge_arr)
