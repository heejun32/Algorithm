import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
not_working = list(input().split())

# 리모콘이 전부 고장나 +, - 로만 조작할 경우 걸리는 횟수
answer = abs(100 - N)

# 모든 채널 경우의 수를 확인, 채널은 무한대이지만 주어진 채널의 최대 숫자는 500,000이다.
# 즉 최대 6자릿수의 숫자 범위를 모두 커버해야 하기 때문에 100만으로 반복문을 설정한다.
for channel in range(1_000_001):
    channel = str(channel)

    # 채널에 포함된 숫자가 작동 안하는지 확인
    for i in range(len(channel)):
        if channel[i] in not_working:
            break
        
        # 채널에 포함와 가장 가까운 숫자(자릿수가 같은)까지 왔다면, 기존 리모콘 조작수와 비교
        elif i == len(channel) - 1:
            answer = min(answer, abs(N - int(channel)) + len(channel))

print(answer)

# 참고 사이트: https://seongonion.tistory.com/99
