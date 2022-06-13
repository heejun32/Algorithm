from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    queue = deque([[A, ""]])
    visited = [False] * 10000
    visited[A] = True

    while queue:
        number, oper = queue.popleft()

        if number == B:
            print(oper)
            break

        # D 연산
        oper_result = 2 * number % 10000
        if not visited[oper_result]:
            visited[oper_result] = True
            queue.append([oper_result, oper + 'D'])

        # L 연산
        oper_result = (number - 1) % 10000
        if not visited[oper_result]:
            visited[oper_result] = True
            queue.append([oper_result, oper + 'S'])

        # L 연산
        temp = 10 * number
        oper_result = temp % 10000 + temp // 10000
        if not visited[oper_result]:
            visited[oper_result] = True
            queue.append([oper_result, oper + 'L'])

        # R 연산
        oper_result = (number % 10 * 1000) + (number // 10)
        if not visited[oper_result]:
            visited[oper_result] = True
            queue.append([oper_result, oper + 'R'])
