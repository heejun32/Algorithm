N, K = map(int, input().split())

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sol(n, k):
    r = factorial(n - k)
    n = factorial(n)
    k = factorial(k)

    answer = n // (k * r)
    return(answer)

print(sol(N, K))