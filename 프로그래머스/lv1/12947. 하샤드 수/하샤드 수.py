def solution(x):
    answer = True
    
    # 자릿수 합 구하기
    _x = x
    digit_sum = 0
    while _x > 0:
        digit_sum += _x % 10
        _x //= 10
    
    # 하샤드 수 확인
    if x % digit_sum != 0:
        answer = False

    return answer