N, X = map(int, input().split())
arr = list(map(int, input().split()))

def solution(N, X, arr):
    for i in range(N):
        if arr[i] < X:
            print(arr[i], end=" ")

solution(N, X, arr)