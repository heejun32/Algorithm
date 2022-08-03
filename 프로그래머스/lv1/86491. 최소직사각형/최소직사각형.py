def solution(sizes):
    # 가로는 가장 긴 길이로 정렬
    for size in sizes:
        w, h = size
        if w < h:
            size[0], size[1] = h, w
    
    w = h = 0
    for size in sizes:
        w = max(w, size[0])
        h = max(h, size[1])
    return w * h