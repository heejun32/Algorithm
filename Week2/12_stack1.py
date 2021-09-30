# 리스트를 사용하여 스택을 구현하는 경우
# 장점: 구현이 용이
# 단점: 리스트의 크기를 변경하는 작업은 내부적으로 overhead 발생 작업으로 많은 시간이 필요
# 해결방법: 리스트의 크기를 배열처럼 고정, 동적 연결 리스트를 이용하여 저장소를 동적으로 할당


# Memoization: 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서
# 매번 다시 계산하지 않도록 하여 전체적인 실행 속도를 빠르게 하는 기술
# 동적 계획법의 핵심이 되는 기술


# 동적계획법:
# 그리디처럼 최적화 문제를 해결하는 알고리즘
# 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 다음 그해들을 이용해 보다 큰 크기의 부분 문제들을 해결
# 최종적으로 원래 주어진 입력의 문제를 해결함

# 예시 피보나치 수 구하기
# 1. 문제를 부분 문제로 분할
# 2. 부분 문제로 나누는 일을 끝내면 가장 작은 부분문제부터 해를 구함
# 3. 해당 결과를 테이블에 저장하고 테이블의 저장된 값을 이용해 상위값을 구함

# DFS, BFS 여기서 스택을 이용하는 DFS를 살펴봄

# stack = []
# def push(item):
#     stack.append(item)
#
# def pop():
#     if (len(stack) == 0):
#         print("Stack is empty!")
#         return
#     else:
#         return stack.pop(-1)
#
# push(1)
# push(2)
# push(3)
#
# print("pop item: ", pop())
# print("pop item: ", pop())
# print("pop item: ", pop())

# DP 문제는 최대한 깊게 이해하고 풀어야 한다.
# 이전 내용들을 복습하고 DP 문제 풀어보기

test_case = int(input())

for test in range(1, test_case + 1):
    HEIGHT = 20         # 세로
    WIDE = int(input()) # 가로

    result = None

    print(f"#{test} {result}")