def solution(n, info):
    answer, tmp = [0] * 11, [0] * 11
    max_diff = 0
    
    for subset in range(1, 1 << 10):
        ryan = apeach = cnt = 0
        
        # 0을 제외한 1~10까지의 원소만 존재
        for i in range(10):
            # 비트 활성화 확인: i번째 원소가 현재 subset에서 활성화된다면
            if subset & (1 << i):
                ryan += 10 - i
                
                # 라이언이 쏴야 하는 화살의 개수는 어피치보다 1개 더 많다.
                tmp[i] = info[i] + 1
                cnt += tmp[i]
            # 아닌 경우 화살을 안쏘면 된다.
            else:
                tmp[i] = 0
                if info[i]:
                    apeach += 10 - i
            
        # 라이언이 쏜 화살수가 n 개를 넘는다면
        if cnt > n: continue

        # 0점에 쏴야할 화살
        tmp[10] = n - cnt

        # 원소 개수 비교
        if ryan - apeach == max_diff:
            for i in reversed(range(11)):
                if tmp[i] > answer[i]:
                    max_diff = ryan - apeach
                    answer = tmp[:]
                    break
                elif tmp[i] < answer[i]:
                    break
        elif ryan - apeach > max_diff:
            max_diff = ryan - apeach
            answer = tmp[:]
    
    # 라이언이 이기지 못하는 경우
    if not max_diff:
        answer = [-1]
    
    return answer