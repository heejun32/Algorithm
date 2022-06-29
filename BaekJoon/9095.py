import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n_list = [0, 1, 2, 4]
    n = int(input())

    if n < 4:
        print(n_list[n])
    else:
        for i in range(4, n+1):
            n_list.append(n_list[i-1] + n_list[i-2] + n_list[i-3])
        print(n_list[n])

# 복습: https://jyami.tistory.com/15
