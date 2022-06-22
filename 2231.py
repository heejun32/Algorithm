N = int(input())
result = 0
total = 0

i = 1
while(i < N + 1):
    digis = list(map(int, str(i)))
    total = i + sum(digis)

    # for j in str(i):
    #     total += int(j)
    #
    if total == N:
        result = i
        break
    i += 1

print(result)