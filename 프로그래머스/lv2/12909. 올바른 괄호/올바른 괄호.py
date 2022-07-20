def solution(s):
    answer = True
    pair = {"(": ")"}
    stack = []
    
    for i in s:
        if i in pair:
            stack.append(i)
        elif not stack or pair[stack[-1]] != i:
            return False
        else:
            stack.pop()
    if stack:
        return False
    return True