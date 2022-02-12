import sys
input = sys.stdin.readline

N = int(input())
N_list = [0, 1, 3]

if N < 3:
    print(N_list[N])
else:
    for i in range(3, N+1):
        N_list.append(N_list[i-1] * 2 - 1)
        print(N_list)
    print(N_list[N])