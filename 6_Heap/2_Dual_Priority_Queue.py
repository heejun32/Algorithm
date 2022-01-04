import heapq


def solution(operations):
    answer = []
    double_queue = []

    while len(operations) != 0:
        param = operations.pop(0)

        if param[0] == "I":
            heapq.heappush(double_queue, int(param[2:]))
            print(double_queue)

        if len(double_queue) == 0:
            continue

        if param == "D 1":
            double_queue.pop()

        if param == "D -1":
            heapq.heappop(double_queue)
            # 큐를 써도 맞음

    if len(double_queue) == 0:
        return [0, 0]

    else:
        answer.append(max(double_queue))
        answer.append(min(double_queue))

    return answer


# 오랜만에 내힘으로 전부 푼 문제. 여기서 min heap의 특징 최솟값이 제일 앞에, 최대 값이 제일 뒤에 있는 것을 활용. 새로운 값이 들어올때마다 대소를 비교해 주기 때문!