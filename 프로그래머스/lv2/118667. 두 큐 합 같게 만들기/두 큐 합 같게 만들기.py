import collections


def solution(queue1, queue2):
    '''
    Time Complexity is O(N)
    Space Complexity is O(N)
    '''
    q1, q2 = collections.deque(queue1), collections.deque(queue2)
    qsum_1, qsum_2 = sum(q1), sum(q2)
    cnt = 0
    
    # 종료 조건1
    while q1 and q1 and cnt <= 3 * len(queue1):
        # 종료 조건2: 정답을 찾은 경우
        if qsum_1 == qsum_2: 
            return cnt
        elif qsum_1 < qsum_2:
            tmp = q2.popleft()
            q1.append(tmp)
            qsum_1 += tmp
            qsum_2 -= tmp
        else:
            tmp = q1.popleft()
            q2.append(tmp)
            qsum_1 -= tmp
            qsum_2 += tmp
        cnt += 1
        # debugging
        # print(q1, q2, cnt)
    return -1