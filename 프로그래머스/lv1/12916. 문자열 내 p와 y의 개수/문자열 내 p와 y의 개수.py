def solution(s):
    p_cnt = y_cnt = 0
    for alpha in s:
        if alpha == 'P' or alpha =='p':
            p_cnt += 1
        elif alpha == 'Y' or alpha =='y':
            y_cnt += 1
    
    # p와 y 모두 하나도 없는 경우
    if (not p_cnt) and (not y_cnt):
        return True
    elif p_cnt == y_cnt:
        return True
    elif p_cnt != y_cnt:
        return False