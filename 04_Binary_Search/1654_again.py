import sys
input = sys.stdin.readline

# 1번 풀이
# K, N = map(int, input().split())
# LAN = [int(input()) for _ in range(K)]

# mean = sum(LAN) // K

# while True:
#     count = 0
#     for i in range(len(LAN)):
#         count += LAN[i] // mean

#     if count != N:
#         mean -= 1

#     if count == N:
#         print(mean)
#         break

K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]

# 랜선을 자를 기준 길이를 이분탐색 하자
low = 1
high = max(LAN)
answer = 0
while low <= high:
    count = 0
    middle = (low + high) // 2
    for i in range(K):
        count += LAN[i] // middle
    
    if count >= N:
        low = middle + 1
        # N개 이상 만들 수 있는 가장 큰 길이 값이어야 한다.
        answer = max(answer, middle)
    else:
        high = middle - 1

print(answer)

# 참고 사이트 https://cocoon1787.tistory.com/288
