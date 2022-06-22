N = int(input())
numbers = list(map(int, input().split()))

min = min(numbers)
max = max(numbers)

# min = numbers[0]
# for i in range(N):
#     if min > numbers[i]:
#         min = numbers[i]
#
# max = numbers[0]
# for i in range(N):
#     if max < numbers[i]:
#         max = numbers[i]

print(f"{min} {max}")