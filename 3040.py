import sys
input = sys.stdin.readline

dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

total = sum(dwarfs)
for i in range(9):
    for j in range(i + 1, 9):
        if total - (dwarfs[i] + dwarfs[j]) == 100:
            dwarf1 = dwarfs[i]
            dwarf2 = dwarfs[j]
            dwarfs.remove(dwarf1)
            dwarfs.remove(dwarf2)
            break
    if len(dwarfs) < 9:
        break

for dwarf in dwarfs:
    print(dwarf)
