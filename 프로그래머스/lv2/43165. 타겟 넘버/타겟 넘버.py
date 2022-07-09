def solution(numbers, target):
    answer = 0
    stack = []
    stack.append([numbers[0], 0])
    stack.append([-1 * numbers[0], 0])
    n = len(numbers)
    
    while (stack):
        value, idx = stack.pop()
        idx += 1
        
        if idx < n:
            stack.append([value + numbers[idx], idx])
            stack.append([value + (-1 * numbers[idx]), idx])
            
        else:
            if target == value:
                answer += 1
    
    return answer