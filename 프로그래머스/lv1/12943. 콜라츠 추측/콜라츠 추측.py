def solution(n):
    # 예외처리
    if n == 1:
        return 0
    
    count = 0
    while n > 1 and count < 500:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        count += 1
    
    if n != 1:
        return -1
    else:
        return count