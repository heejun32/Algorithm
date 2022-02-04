from collections import deque
import sys
input = sys.stdin.readline

# https://re-code-cord.tistory.com/entry/%EB%B0%B1%EC%A4%80-5430%EB%B2%88-AC-Python?category=980167
T = int(input())
for _ in range(T):
        operations = input().strip()
        n = int(input())
        arr = deque(input()[1:-2].split(','))
        
        R_c = 0
        error = 0
        for oper in operations:
            if oper == 'R':
                R_c += 1
            if oper == 'D':
                if len(arr) < 1:
                    print('error')
                    error += 1
                    break
                elif R_c % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

        if error < 1:
            if R_c % 2 == 1:
                arr.reverse()
            print('[' + ','.join(arr) + ']')


# 틀린데 찾기