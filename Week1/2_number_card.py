test_cases = int(input())

for test_case in range(test_cases):
    N = int(input())
    aj = input().strip()

    aj_list = []
    for i in range(len(aj)):
        aj_list.append(int(aj[i]))

    count_list = [0] * 10
    for i in range(N):
        count_list[aj_list[i]] += 1

    max = 0
    count = 0
    for i in range(len(count_list)):
        if count_list[i] >= max:
            max = count_list[i]
            count = i

    print("#{} {} {}".format(test_case + 1, count, max))
