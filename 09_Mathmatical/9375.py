import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cloths = {}
    for _ in range(n):
        cloth = list(map(str, input().split()))[-1]
        cloths[cloth] = cloths.get(cloth, 1) + 1

    answer = 1
    cloths_list = list(cloths.values())
    for i in range(len(cloths_list)):
        answer *= cloths_list[i]

    print(answer - 1)
