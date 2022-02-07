import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.insert(0, 0)
acc_list = [0] * (N + 1)
# 누적합 리스트 생성

# print(N_list)
for i in range(1, N + 1):
    acc_list[i] = N_list[i] + acc_list[i - 1]
# print(acc_list)

for _ in range(M):
    i, j = map(int, input().split())

    if i == j:
        print(N_list[i])
    
    elif i == 1:
        print(acc_list[j])
    
    else:
        i -= 1
        print(acc_list[j]-acc_list[i])