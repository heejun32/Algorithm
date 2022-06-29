import sys
input = sys.stdin.readline

#  문제를 제대로 읽고, 이해하자...
N = int(input())
hansu = 0

for i in range(1, N + 1):
    if i < 100:
        hansu += 1
    else:
        number = list(map(int, str(i)))  # 숫자 -> 문자열 치환 -> 리스트화
        if int(number[1]) - int(number[0]) == int(number[2]) - int(number[1]):
            hansu += 1

print(hansu)
