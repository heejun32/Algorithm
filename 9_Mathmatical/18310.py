N = int(input())
locations = list(map(int, input().split()))
locations.sort()

if N % 2 == 0:
    answer = locations[N // 2 - 1]
else:
    answer = locations[N // 2]

print(answer)
