from collections import OrderedDict


def solution(numbers):
    answer = 0
    # 순서대로 정렬
    numbers.sort()
    
    # 사전으로 카운트 해주기
    num_dict = OrderedDict()
    for number in numbers:
        num_dict[number] = 1

    for i in range(10):
        if i not in num_dict:
            answer += i
    
    
    return answer