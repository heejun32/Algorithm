import sys
input = sys.stdin.readline

K = int(input())

stack = []
for _ in range(K):
    integer = int(input())

    if integer == 0:
        stack.pop()
    else:
        stack.append(integer)

print(sum(stack))