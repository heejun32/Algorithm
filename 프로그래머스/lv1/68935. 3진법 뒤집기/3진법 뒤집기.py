def solution(n):
    answer = 0

    # 3진법으로 작성, 처음부터 역수로 작성
    thr = []
    while n:
        thr.append(n % 3)
        n //= 3
    
    # 10진법으로 게산
    print(thr)
    for e, value in enumerate(thr):
        e = len(thr) - 1 - e
        answer += value * (3 ** e)
    return answer