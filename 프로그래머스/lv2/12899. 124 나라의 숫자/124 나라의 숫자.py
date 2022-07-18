def solution(n):
    answer = ''
    # 10진법 1, 2, 3 일때 패턴 확인
    notation = ['4', '1', '2']
    
    # 124진법 변환 시작
    while n:
        answer = notation[n % 3] + answer
        # 3으로 나눠 떨어지면
        if not (n % 3):    
            n = n // 3 - 1
        else:
            n = n // 3
    
    return answer