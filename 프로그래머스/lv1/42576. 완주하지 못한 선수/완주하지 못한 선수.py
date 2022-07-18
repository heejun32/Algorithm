from collections import Counter


def solution(participant, completion):
    answer = ''
    counter = Counter(completion)
    
    for p in participant:
        if p not in counter or counter[p] == 0:
            answer += p
        else:
            counter[p] -= 1
    return answer