# 2630 문제와 차이: answer list자료형은 주소를, 변수는 주소를 그래서 접근이~~

import sys
input = sys.stdin.readline

N = int(input())
IMAGE = [input().strip() for _ in range(N)]
answer = ""


def comp(x, y, N):
    check = IMAGE[x][y]
    global answer
    for row in range(x, x + N):
        for col in range(y, y + N):
            if check != IMAGE[row][col]:
                answer += '('
                # 1사분면
                comp(x, y, N // 2)
                # 2사분면
                comp(x, y + N // 2 , N // 2)
                # 3사분면
                comp(x + N // 2, y , N // 2)
                # 4사분면
                comp(x + N // 2, y + N // 2, N // 2)
                answer += ')'
                return None
    if check == '0':
        answer += '0'
    else:
        answer += '1'
    return None


comp(0, 0, N)
print(answer)
