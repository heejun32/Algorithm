import sys

def factorial(N):
    total = 1
    if N == 1 or N == 0:
        return 1
    while N > 1:
        total = total * N
        N -= 1
    return total

input = sys.stdin.readline
N = int(input())
total = factorial(N)
zeros = 0

while (total % 10 == 0):
    zeros += 1
    total //= 10

print(zeros)