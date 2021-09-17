def binary_search(start, end, target, count):
    middle = (start + end) // 2
    if middle == target:
        return count
    if target > middle:
        return binary_search(middle, end, target, count + 1)
    else:
        return binary_search(start, middle, target, count + 1)

test_cases = int(input().strip())
for test_case in range(test_cases):
    P, A, B = map(int, input().strip().split())
    countA = binary_search(1, P, A, 0)
    countB = binary_search(1, P, B, 0)

    # ps1, pe1 = 1, P
    # ps2, pe2 = 1, P
    # count1 = 0
    # count2 = 0
    #
    # while (1):
    #     count1 = count1 + 1
    #     if Pa == ps1 or Pa == pe1:
    #         break
    #     middle = int((pe1 + ps1) / 2)
    #     if Pa > middle:
    #         ps1 = middle
    #     else:
    #         pe1 = middle
    #
    # while (1):
    #     count2 = count2 + 1
    #     if Pb == ps2 or Pb == pe2:
    #         break
    #     middle = int((pe2 + ps2) / 2)
    #     if Pb > middle:
    #         ps2 = middle
    #     else:
    #         pe2 = middle

    if countA < countB:
        print(f"#{test_case + 1} A")
    elif countA > countB:
        print(f"#{test_case + 1} B")
    else:
        print(f"#{test_case + 1} 0")

# 재귀함수 활용가능.