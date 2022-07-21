def gcd(w, h):
    while h:
        n = w % h
        w = h
        h = n
    return w


def solution(w,h):
    return (w * h) - (w + h - gcd(w, h))