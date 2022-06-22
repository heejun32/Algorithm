# 1     7      19       37        61
# an = an-1 + 6(n-1)

N = int(input())
passed = 1
i = 1
jump = 1

while i < N:
    passed += 1
    i = i + 6 * jump
    jump += 1

print(passed)
