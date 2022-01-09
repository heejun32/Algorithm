N = int(input())

for i in range(N):
    result = input()
    o_grade = 1
    total = 0

    for j in result:
        if j == 'O':
            total += o_grade
            o_grade += 1

        if j == "X":
            o_grade = 1

    print(total)