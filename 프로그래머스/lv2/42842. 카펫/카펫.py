def solution(brown, yellow):
    s = brown + yellow
    
    for width in range(s, 0, -1):
        height = s // width
        y = (width - 2) * (height - 2)
        b = s - y
        if y == yellow and b == brown:
            return [width, height]
            break
    

