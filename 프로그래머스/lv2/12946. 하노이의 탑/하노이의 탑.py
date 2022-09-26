from typing import List

def solution(n: int) -> List[List[int]]:
    answer = []
    
    def hanoi(n, start, end, via):
        if n == 1:
            answer.append([start, end])
            return None
        else:
            hanoi(n - 1, start, via, end)
            answer.append([start, end])
            hanoi(n - 1, via, end, start)

    hanoi(n, 1, 3, 2)

    return answer