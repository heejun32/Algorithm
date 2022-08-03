def gcd(a, b):
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a

def solution(n, m):
    _gcd = gcd(n, m)
    lcm = n * m / _gcd
    return [_gcd, lcm]