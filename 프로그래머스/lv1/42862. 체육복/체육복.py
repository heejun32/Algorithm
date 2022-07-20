# from collections import defaultdict


# def solution(n, lost, reserve):
#     answer = 0
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
# #     _reserve.sort()
# #     _lost.sort()
    
#     # 여분의 체육복 가진 학생들 dict형으로 만들기
#     _reserve_dict = defaultdict(int)
#     for r in _reserve:
#         _reserve_dict[r] = 2

#     # 체육복이 없는 학생을 기준으로 탐색
#     for l in _lost:
#         if l-1 in _reserve_dict:
#             if _reserve_dict[l-1] > 1:  
#                 _reserve_dict[l-1] -= 1
#                 answer += 1
#         elif l+1 in _reserve_dict: 
#             if _reserve_dict[l+1] > 1:
#                 _reserve_dict[l+1] -= 1
#                 answer += 1
#     answer = n - len(_lost) + answer
#     return answer
# def solution(n, lost, reserve):
def solution(n, lost, reserve):
    realLost = list(set(lost) - set(reserve))
    realReserve = list(set(reserve) - set(lost))
    realLost.sort()
    realReserve.sort()
    lostCount = len(realLost)
    for lostStudent in realLost:
        if lostStudent-1 in realReserve:
            lostCount-=1
            realReserve.remove(lostStudent-1)
        elif lostStudent+1 in realReserve:
            lostCount-=1
            realReserve.remove(lostStudent+1)
    return n-lostCount