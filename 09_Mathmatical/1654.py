import sys
input = sys.stdin.readline

dict = {}
alphabet = 'a'
for i in range(1, 27):
    dict[alphabet] = dict.get(alphabet, i)
    alphabet = chr(ord(alphabet) + 1)

r = 31
M = 1234567891
L = int(input())
string = input().strip()

answer = 0
multiplier = 0
for alphabet in string:
    answer += dict[alphabet] * (r ** multiplier)
    multiplier += 1

print(answer % M)