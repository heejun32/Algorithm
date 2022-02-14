def solution(tickets):
    # 1. 경로 사전 생성
    routes = dict()

    for start, end in tickets:
        if start in routes:
            routes[start].append(end)
        else:
            routes[start] = [end]

    # 2. 시작점 - [끝점] 역순 정렬
    for start in routes.keys():
        routes[start].sort(reverse=True)

    # DFS 알고리즘을 path로 생성
    stack = ['ICN']
    answer = []

    while (stack):
        top = stack[-1]

        if top not in routes or len(routes[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top].pop()
            # routes[top] = routes[top][:-1] # 값 삭제

    return answer[::-1] #현재 answer은 제일 먼저 방문한 공항이 제일 뒤에 위치해 있기 때문.


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# 문제 잘 못이해, 모든 티켓을 다써야 하기에 각 티켓으로 연결되어 있는 최대 경로를 다 방문해야함 DFS!
# 풀이 초반 사전을 통해 그래프 경로를 생성하긴 했지만 이후 접근 방법에 대해서는 상당히 해맴...
# 참고: https://gurumee92.tistory.com/165