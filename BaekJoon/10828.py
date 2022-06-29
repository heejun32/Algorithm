import sys

input = sys.stdin.readline
N = int(input())

def push(stack, X):
    stack.append(X)
    return stack

def pop(stack):
    if len(stack) == 0:
        print(-1)
        return stack
    else:
        print(stack.pop())
        return stack

def size(stack):
    print(len(stack))

def empty(stack):
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


stack = []
for _ in range(N):
    question = list(input().split())

    if question[0] == "push":
        stack = push(stack, question[1])

    if question[0] == "top":
        top(stack)

    if question[0] == "size":
        size(stack)

    if question[0] == "pop":
        stack = pop(stack)

    if question[0] == "empty":
        empty(stack)




