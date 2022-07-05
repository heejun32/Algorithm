import sys
input = sys.stdin.readline
N = int(input())
numbers = {}

for _ in range(N):
    key = int(input())
    numbers[key] = numbers.get(key, 0) + 1

keys = sorted(numbers.keys())
for key in keys:
    while numbers[key] > 0:
        print(key)
        numbers[key] -= 1