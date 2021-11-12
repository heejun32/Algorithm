def solution(n, times):
    times.sort()                # 심사가 제일 적게 걸리는 사람순으로 정렬
    answer  = 0
    left    = 1                 # 최소 심사 시간
    right   = max(times) * n    # 최대 심사 시간

    while (left <= right):
        passenger = 0           # 심사가 완료된 사람수
        mid       = (left + right) // 2

        for time in times:
            passenger += mid // time

        if passenger >= n:      # 여기서 정답이 걸리기 때문에 answer를 설정함
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer