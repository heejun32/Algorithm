M, N = map(int, input().split())

def prime_number(n : int):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(M : int, N : int):
    for n in range(M, N + 1):
        if prime_number(n):
            print(n)

solution(M, N)