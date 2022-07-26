def solution(numbers, target):
    answer = 0
    result = [0]
    
    for num in numbers:
        temp = []
        for r in result:
            temp.append(r + num)
            temp.append(r - num)
        result = temp
        
    for r in result:
        if r == target:
            answer += 1
    return answer
