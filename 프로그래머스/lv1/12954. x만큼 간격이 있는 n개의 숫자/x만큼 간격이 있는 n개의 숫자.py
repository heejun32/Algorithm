def solution(x, n):
    answer = []
    temp = x
    while len(answer) != n:
        answer.append(temp)
        temp += x
    return answer
