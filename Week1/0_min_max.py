test_cases = int(input())
for test_case in range(test_cases):
    counts = int(input())
    arr = []

    for num in list((input().strip().split())):
        arr.append(int(num))

    min = arr[0]
    for count in range(counts):
        if min > arr[count]:
            min = arr[count]

    max = arr[0]
    for count in range(counts):
        if max < arr[count]:
            max = arr[count]

    print("#{} {}".format(test_case + 1, max - min))