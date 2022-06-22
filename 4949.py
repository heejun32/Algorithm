import sys
input = sys.stdin.readline

while 1:
    s = input().rstrip()
    stack = []

    # 종료 조건
    if s == '.':
        break

    for w in s:
        if w == '(' or w =='[':
            stack.append(w)
        
        if w == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(w)
        
        if w == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(w)

    if stack:
        print('no')
    else:
        print('yes')