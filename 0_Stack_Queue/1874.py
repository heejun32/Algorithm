import sys
input = sys.stdin.readline
N = int(input())
M = []
for _ in range(N):
    M.append(int(input()))
n = [i for i in range(N, 0, -1)]
stack = []
stack_cal = []
stack_sequence = []
# ================================================= 변수 초기화

stack.append(n.pop())
stack_cal.append('+')

# ================================================== 스택 수열 찾기
i = 0
while n:
    if not stack:
        stack.append(n.pop())
        stack_cal.append('+')

    if stack[-1] == M[i]:
        i += 1
        stack_sequence.append(stack.pop())
        stack_cal.append('-')
        continue

    stack.append(n.pop())
    stack_cal.append('+')

while stack:
    stack_sequence.append(stack.pop())
    stack_cal.append('-')

if stack_sequence == M:
    for i in stack_cal:
        print(i)
else:
    print("NO")