import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
max_lenght = float('-inf')
count = 2

for i in range(N - 2):
    if (A[i] <= A[i + 1] <= A[i + 2]) or (A[i] >= A[i + 1] >= A[i + 2]):
        count = 2
    else:
        count += 1
    max_lenght = max(max_lenght, count)

print(max_lenght)
