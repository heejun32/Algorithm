import sys
input = sys.stdin.readline

N, x = map(int, input().split())
lst = list(map(int, input().split()))

# x보다 작고 0~x보다 작은수의 인덱스, x보다 크고 배열의 끝인 인덱스를 구해서 전체 길이에서 빼주면?


start = 0
end = N - 1
left = 0
right = 0
while start <= end:
    middle = (start + end) // 2
    if lst[middle] == x:
        end = middle - 1
    elif lst[middle] < x:
        left = max(left, middle)
        start = middle + 1

start = 0
end = N - 1
while start <= end:
    middle = (start + end) // 2
    if lst[middle] == x:
        start = middle + 1
    elif lst[middle] > x:
        right = max(right, middle)
        end = middle - 1

print(N - (left + 1) - (N - right))
