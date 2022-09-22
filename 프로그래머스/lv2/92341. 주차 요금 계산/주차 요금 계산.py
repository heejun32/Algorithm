from typing import List
import collections
import math


def solution(fees: List[int], records: List[str]) -> List[int]:
    answer = []
    '''
    cars_in = {차량 번호: [입차 시간]}
    cars_out = # {차량 번호: 주차 시간}
    '''
    cars_in, cars_out = collections.defaultdict(list), collections.defaultdict(int)
    
    for record in records:
        
        # 시간, 차 번호, 입출차 여부
        time, num, in_out = record.split()
        if in_out == "IN":
            cars_in[num].append(time)
        else:
            in_hour, in_min = map(int, cars_in[num].pop().split(":"))
            out_hour, out_min = map(int, time.split(":"))
            
            # 분 계산
            if out_min < in_min:
                out_hour -= 1
                out_min += 60
                
            # 총 주차 시간 계산            
            total_min = 60 * (out_hour - in_hour) + (out_min - in_min)
            cars_out[num] += total_min
    
    # 출차 되지 않은 차 처리
    for num in cars_in.keys():
        if cars_in[num]:
            in_hour, in_min = map(int, cars_in[num].pop().split(":"))
            total_min = 60 * (23 - in_hour) + (59 - in_min)
            cars_out[num] += total_min
    
    # 주차 요금 계산 fees = [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
    for num in sorted(cars_out.keys()):
        if cars_out[num] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + int(math.ceil((cars_out[num] - fees[0]) / fees[2])) * fees[3])

    return answer