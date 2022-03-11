import sys
input = sys.stdin.readline

dwarfs = [int(input()) for _ in range(9)]
total = sum(dwarfs)

for i in range(9):
    for j in range(i + 1, 9):
        if total - (dwarfs[i] + dwarfs[j]) == 100:
            num1 = dwarfs[i]
            num2 = dwarfs[j]
            dwarfs.remove(num1)
            dwarfs.remove(num2)
            dwarfs.sort()
            for dwarf in dwarfs:
                print(dwarf)
            break
    #  중복 반복문을 빠져나오는 조건을 추가로 생각해주기
    if len(dwarfs) < 9:
        break
 