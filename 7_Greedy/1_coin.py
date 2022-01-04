N, K = map(int, input().split())
coins = []
answer = 0

for i in range(N):
    coins.append(int(input()))

for i in range(len(coins) - 1, -1, -1):
    if K // coins[i] == 0:
        continue
    elif K // coins[i] != 0:
        answer += K // coins[i]
        K = K - (K // coins[i]) * coins[i]

print(answer)