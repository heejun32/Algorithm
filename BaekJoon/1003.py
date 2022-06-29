import sys
input = sys.stdin.readline
T = int(input())

def fibonnaci_func(n):
    zeros = [1, 0]
    ones = [0, 1]

    while n > 1:
        zeros.append(zeros[-1] + zeros[-2])
        ones.append(ones[-1] + ones[-2])
        n -= 1

    if n == 0:
        print(f"{zeros[-2]} {ones[-2]}")
    else:
        print(f"{zeros[-1]} {ones[-1]}")

for _ in range(T):
    n = int(input())
    fibonnaci_func(n)