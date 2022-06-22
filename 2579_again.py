'''
패턴 확인
1 2 3 4
O X O O  => d[i] = stairs[i] + stairs[i - 1] + dp[i-3]
O O X O  => d[i] = stairs[i] + dp[i-2]
'''

import sys
input = sys.stdin.readline

N = int(input())
stairs = []
for n in range(N):
    stairs.append(int(input()))
dp = [0] * N

if N == 1:
    dp[0] = stairs[0]
if N == 2:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
if N >= 3:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[2] + stairs[1], stairs[2] + stairs[0])

for i in range(3, N):
    dp[i] = max(stairs[i] + stairs[i - 1] + dp[i-3], stairs[i] + dp[i-2])

print(dp[-1])
