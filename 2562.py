def sol():
    lst = [0] * 9

    for i in range(9):
        lst[i] = int(input())

    start = max(lst)

    for i in range(9):
        if start == lst[i]:
            print(start)
            print(i + 1)

sol()