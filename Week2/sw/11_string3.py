# TEST_CASE = int(input())
#
# for test in range(1, TEST_CASE + 1):
#     str1 = input()
#     str2 = input()
#
#     str1_count = [0] * len(str1)
#
#     for i in range(len(str1)):
#         for j in range(len(str2)):
#             if str1[i] == str2[j]:
#                 str1_count[i] = str1_count[i] + 1
#
#     print(f"#{test} {max(str1_count)}")

# 문제에서 딕셔너리 활용을 팁으로 줬기에 사용해보자

TEST_CASE = int(input())

for test in range(1, TEST_CASE + 1):
    str1 = input()
    str2 = input()

    dict = {}
    for i in str1:
        dict[i] = 0

    for j in str2:
        if j in dict:
            dict[j] = + dict[j] + 1
    print(f"#{test} {max(dict.values())}")