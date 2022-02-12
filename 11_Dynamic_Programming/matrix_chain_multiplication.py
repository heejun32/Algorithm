'''
References
1. https://www.youtube.com/watch?v=8Ni1gaP35i8
2. https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/
'''
import sys
maxint=int(1e9+7)

def MatrixChainOrder(p, n):
    # 행렬 인덱스 접근을 편하게 하기 위해 n * n 2차원 배열 생성
    m = [[0 for x in range(n)] for x in range(n)] 
 
    # 행렬이 1개인 경우 연산 결과를 바로 전달
    for i in range(1, n):
        m[i][i] = 0
 
    for L in range(2, n):
        for i in range(1, n-L + 1): # (n-i) * i 의 n-i: chain 횟수 의미
            j = i + L-1             # (n-i) * i 의 i 상수를 의미, i < j
            m[i][j] = maxint
            for k in range(i, j):
                # q = cost / scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                
                # 연산 과정 확인
                for r in m:
                    print(r)
                print()
 
    return m[1][n-1]
 
# Code Test
arr = [20, 5, 40, 50, 10]
size = len(arr)
print("Minimum number of multiplications is " + str(MatrixChainOrder(arr, size)))