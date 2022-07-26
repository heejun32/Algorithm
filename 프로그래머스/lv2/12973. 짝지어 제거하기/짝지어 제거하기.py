def solution(s):
    answer = 0
    stack = []
    for alpha in s:
        if not stack:
            stack.append(alpha)
        elif stack[-1] == alpha:
            stack.pop()
        else:
            stack.append(alpha)

    if not stack:
        answer = 1
    return answer