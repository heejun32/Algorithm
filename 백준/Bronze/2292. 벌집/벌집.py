N = int(input())
passed = 1
i = 1
jump = 1

while i < N:
    passed += 1
    i = i + 6 * jump
    jump += 1

print(passed)