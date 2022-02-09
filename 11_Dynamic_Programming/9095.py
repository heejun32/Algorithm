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

# 복습: https://pacific-ocean.tistory.com/192
# https://velog.io/@i-zro/%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%BD%94%ED%85%8C-%EB%8C%80%EB%B9%84-DP-%EB%B0%B1%EC%A4%80-9095-1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0