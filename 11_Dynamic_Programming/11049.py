# flake8 코드 스타일이 적용되어 있습니다.
import sys
input = sys.stdin.readline
maxint = sys.maxsize


def MatrixChainOrder(p, n):
    # 행렬 인덱스 접근을 편하게 하기 위해 행렬 개수 + 1 크기의 2차원 배열 생성
    m = [[0 for x in range(n)] for x in range(n)]

    # 행렬이 1개 들어올 경우 바로 출력하기 위해 작성. 연산 횟수는 0
    for i in range(1, n):
        m[i][i] = 0

    # L is chain length.
    for L in range(2, n):  # n-i번의 연산
        for i in range(1, n-L + 1):  # 상수 연산(row 결정)
            j = i + L-1              # i <= j, but 자기 자신의 자리는 0
            m[i][j] = maxint
            for k in range(i, j):
                # q = cost / scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n-1]


N = int(input())
p = []  # 행렬의 앞무분만

# 행렬 정보 입력 받기, 마지막 행렬의 경우 열의 정보까지 필요
for i in range(N):
    r, c = map(int, input().split())
    if i == N - 1:
        p.append(r)
        p.append(c)
    else:
        p.append(r)

answer = MatrixChainOrder(p, len(p))
print(answer)
