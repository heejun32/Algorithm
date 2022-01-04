import heapq


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]]) # 가장 작업 시간이 짧고, 요청이 먼저 온 것을 처리하면 된다!
                print(heap)

        if len(heap) > 0:
            current = heapq.heappop(heap)
            print("current: ", current)
            start = now
            print("start: ", start)
            now += current[0]
            print("now: ", now)
            answer += (now - current[1])
            print("answer: ", answer)
            i += 1

        else:
            now += 1

    return answer // len(jobs)