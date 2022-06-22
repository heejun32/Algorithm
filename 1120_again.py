import sys
input = sys.stdin.readline

A, B = input().strip().split()
diff = []

for i in range(len(B) - len(A) + 1):
    count = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            count += 1
    diff.append(count)

print(min(diff))
