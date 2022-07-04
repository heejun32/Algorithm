import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
         a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def cal(M, N, x, y):
    end = lcm(M, N)
    k = x
    while k <= end:
        if (k - x) % M == 0 and (k - y) % N == 0:
            return k
        k += M
    return -1


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(cal(M, N, x, y))
