import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    apartment = [room for room in range(1, n + 1)]

    for floor in range(k):
        for room in range(1, n):
            apartment[room] += apartment[room - 1]
    
    print(apartment[n-1])