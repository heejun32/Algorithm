N = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(list(set(arr)))
answer_dict = {}

for i in range(len(sort_arr)):
    answer_dict[sort_arr[i]] = i

for i in range(N):
    arr[i] = answer_dict[arr[i]]

for i in range(N):
    print(arr[i], end=" ")
