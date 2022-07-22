from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    time = 1
    
    # 과정이 다 끝날때까지 반복
    while progresses:
        count = 0
        # 중간에 완료된 작업이 있는지 확인
        while progresses:
            if progresses[0] + speeds[0] * time >= 100:
                progresses.popleft()
                speeds.popleft()
                count += 1
            else:
                time += 1
                break
        # 완료된 작업이 있으면 저장
        if count:
            answer.append(count)

    return answer