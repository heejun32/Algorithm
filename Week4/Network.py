def DFS(node, computers, is_visit):
    stack = []
    stack.append(computers[node])
    is_visit[node] = True

    while(stack):
        # print(stack)
        temp = stack.pop()

        for i in range(len(temp)):
            if is_visit[i] == False and temp[i] == 1: # 연결성이 있으면 방문
                is_visit[i] = True
                stack.append(computers[i])

def solution(n, computers):
    is_visit = [False] * n
    answer = 0

    for node in range(n):
        if not is_visit[node]:
            DFS(node, computers, is_visit)
            # print(is_visit)
            answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# 테스트 케이스 457못 넘은 어디서 잘못된 것일까?
# 문제의 접근법이 계속해서 잘못됨. DFS와 BFS는 전부 그래프(트리) 순회 방법임
# 노드를 순회하면서 각 문제의 조건을 어떻게 충족시킬지 연결시킬 것