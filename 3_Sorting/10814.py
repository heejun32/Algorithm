import sys
input = sys.stdin.readline
N = int(input())
information = []

for order in range(1, N + 1):
    age, name = input().split()
    information.append([int(age), name, order])

for info1 in range(len(information) - 1):
    for info2 in range(info1 + 1, len(information)):
        if information[info1][0] > information[info2][0]: # 나이가 같으면 order를 본다!
            temp = information[info1]
            information[info1] = information[info2]
            information[info2] = temp
        if information[info1][0] == information[info2][0]:
            if information[info1][2] > information[info2][2]:
                temp = information[info1]
                information[info1] = information[info2]
                information[info2] = temp

for info in information:
    print(f"{info[0]} {info[1]}")