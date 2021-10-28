# dequeue를 사용하지 않고 리스트로 큐를 구현했을 때 런타임 에러 발생.
# 이유: 리스트로 큐를 구현시 pop()의 시간복잡도는 O(1), pop(0)은 O(N)
''''
def solution(numbers, target):
    answer = 0
    queue = []
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
    n = len(numbers)

    while(queue):
        pop_val = queue.pop(0)
        temp = pop_val[0]
        idx = pop_val[1]
        idx += 1

        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp + -1 * numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer
'''

# BFS 구조
'''
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])

    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer
'''

# DFS 구현
# 이 문제는 결국 주어진 numbers의 모든 경우의 수를 확인해야 하기 때문에 트리의 마지막 노드들을 전부 확인해야함. 따라서 DFS와 BFS 구현의 차이는 없다고 생각됨.
# 인덱스(이론상으로는 트리의 height)를 넘겨주기에 방문 기록을 따로 표시할 이유가 없음.
def solution(numbers, target):
    answer = 0
    stack = []
    stack.append([numbers[0], 0])
    stack.append([-1 * numbers[0], 0])
    n = len(numbers)

    while(stack):
        temp, idx = stack.pop()
        idx += 1

        if idx < n:
            stack.append([temp + numbers[idx], idx])
            stack.append([temp -1 * numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

print(solution([1, 1, 1, 1, 1,], 3))
