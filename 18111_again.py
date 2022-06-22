import sys
input = sys.stdin.readline

# 문제 데이터 입력 받기
N, M, B = map(int, input().split())
LAND = [list(map(int, input().split())) for _ in range(N)]

# 브루트포스트 탐색 시작
answer_time = sys.maxsize
answer_h = 0
# 블록의 높이 범위는 0 ~ 256
for h in range(257):
    build = 0
    remove = 0
    for row in range(N):
        for col in range(M):
            work = LAND[row][col] - h
            # 우리기 부숴야될 블록수
            if work > 0:
                remove += work
            # 우리가 지어야될 블록수
            elif work < 0:
                build -= work
    # 부순 블록 + 가지고 있는 블록수가 지어야될 블록수보다 많다면
    if remove + B >= build:
        time = (remove * 2) + build
        if answer_time >= time:
            answer_time = time
            answer_height = h

print(answer_time, answer_height)


''' 참고 사이트
https://codecollector.tistory.com/678
https://www.acmicpc.net/board/view/86190
'''