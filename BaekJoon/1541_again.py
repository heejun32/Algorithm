import sys
input = sys.stdin.readline

expression = list(input().split('-'))
S = 0

# -로 괄호를 쳐서 나눈 수 중 첫번째 괄호 부분 계산
for i in expression[0].split('+'):
    S += int(i)

# 두번째 괄호부터는 첫번째 괄호에서 값을 빼기
for i in expression[1:]:
    for j in i.split('+'):
        S -= int(j)

print(S)