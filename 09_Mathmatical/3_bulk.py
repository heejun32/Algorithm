N = int(input())
arr = []
rate = [1] * N

for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rate[i] += 1

for i in range(len(rate)):
    print(rate[i], end=" ")