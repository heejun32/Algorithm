# def find_str(str1, str2):
#     answer = len(str1)
#     if len(str1) > len(str2):
#         return 0
#     for j in range(len(str2)):
#         count = 0
#         trace = j
#         for i in range(len(str1)):
#             if str1[i] == str2[trace]:
#                 count = count + 1
#                 trace = trace + 1
#         if count == answer:
#             return 1
#
#     return 0
#
# test_cases = int(input().strip())
# for test_case in range(test_cases):
#     str1 = input().strip()
#     str2 = input().strip()
#
#     answer = find_str(str1, str2)
#
#     print(f"#{test_case + 1} {answer}")
# 오류 코드

TEST_CASE = int(input())

for test in range(1, TEST_CASE + 1):
    str1 = input()
    str2 = input()
    result = 0

    for i in range(len(str2) - len(str1) + 1):
        # 핵심구문 str1이 str2보다 항상 짧다고 가정하면, str1의 길이만큼이 항상 검색되어야 하기에, 굳이 str2를 끝까지 하나하나 비교할 필요 없음.
        if str2[i:i+len(str1)] == str1:
            result = 1
    print(f"#{test} {result}")

# 너무 복잡하게 생각하지말자...