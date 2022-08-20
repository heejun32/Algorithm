def solution(clothes):
    answer = 1
    close = {}
    
    for element in clothes:
        key = element[1]
        value = element[0]
        if key in close.keys():
            close[key].append(value)
        else:
            close[key] = [value]
            
    
    for key in close.keys():
        answer = answer * (len(close[key]) + 1)

    
    return answer - 1