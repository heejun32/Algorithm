from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
        operations = input().strip()
        n = int(input())
        arr = deque(input()[1:-2].split(','))

        if n == 0:
            arr = []
        
        error = False
        R_c = 0        
        for oper in operations:
            if oper == 'R':
                R_c += 1
            if oper == 'D':
                if len(arr) < 1:
                    print('error')
                    error = True
                    break
                elif R_c % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

        if not error:
            if R_c % 2 == 1:
                arr.reverse()
            print('[' + ','.join(arr) + ']')

# 빈 []값을 문자열로 받고 list화 만들면 [''] 값이 들어가기에 빈 배열 초기화가 필요!