import sys
input = sys.stdin.readline

N = int(input())
locations = []

for _ in range(N):
    x, y = map(int, input().split())
    locations.append([x, y])

locations.sort(key=lambda x:(x[0], x[1]))

for location in locations:
    x = location[0]
    y = location[1]
    print(f"{x} {y}")