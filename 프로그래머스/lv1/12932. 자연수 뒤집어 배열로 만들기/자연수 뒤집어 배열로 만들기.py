def solution(n):
    n = str(n)
    answer = [0] * len(n)    
    for i in range(len(n) // 2 + 1):
        answer[i], answer[len(n) - 1 - i] = int(n[len(n) - 1 - i]), int(n[i])
        
    
    return answer