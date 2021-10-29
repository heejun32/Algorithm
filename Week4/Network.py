def solution(n, computers):
    is_visit = [0] * n
    stack = []
    answer = 0

    for node in range(n):
        stack.append(computers[node])
        temp = stack.pop()

        for i in range(n):
            if temp[i] == 1:
                is_visit[i] += 1
                stack.append(computers[i])

    for i in is_visit:
        if i == 1:
            answer += 1
    return answer + 1

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# 테스트 케이스 457못 넘은 어디서 잘못된 것일까?