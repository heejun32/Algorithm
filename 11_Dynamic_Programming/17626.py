N = int(input())
answer = 0

while N > 1:
    answer += 1
    num = int(N ** 0.5)
    print(num)
    N = N - num * num

print(answer)
