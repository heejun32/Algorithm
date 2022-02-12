T = int(input())

for _ in range(T):
    k = int(input()) #1 ~ 14
    n = int(input()) #1 ~ 14


# 3층 1 5 15   4  10
# 2층 1 4 10   3  6
# 1층 1 3 6    2  3
# 0층 1 2 3    1  1
    people = 0
    i = 0
    while i < k:
        for j in range(1, n + 1):
            people += j

        i += 1

    print(people)
