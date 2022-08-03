def solution(s, n):
    answer = ''
    for alpha in s:
        if alpha.isupper():
            alpha = chr((ord(alpha) - ord('A') + n) % 26 + ord('A'))
        elif alpha.islower():
            alpha = chr((ord(alpha) - ord('a') + n) % 26 + ord('a'))
        answer += alpha
    return answer