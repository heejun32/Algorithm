import sys
input = sys.stdin.readline
N = int(input())
info = []

for order in range(1, N + 1):
    age, name = input().split()
    age = int(age)
    info.append([age, name, order])

info.sort(key=lambda x:(x[0], x[2]))

for i in info:
    print(f"{i[0]} {i[1]}")