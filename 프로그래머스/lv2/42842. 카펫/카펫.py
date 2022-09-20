def solution(brown, yellow):
    '''
    (가로 - 2) * (세로 - 2) == 노란색 격자 수
    가로 * 세로 - 노란색 격자 수 == 갈색 격자 수
    '''

    # 가로, 세로
    answer = []
    
    for wide in range(5000):
        for height in range(5000):
            if wide < height:
                break
            y_r2 = (wide - 2) * (height - 2)             
            if y_r2 == yellow and wide * height - y_r2 == brown:
                return [wide, height]

    return answer