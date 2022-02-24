import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split(':'))
standard = n
if n > m:
    standard = m

for i in range(standard, 0, -1):
    if n % i == 0 and m % i == 0:
        n //= i 
        m //= i
        print(f'{n}:{m}')
        break