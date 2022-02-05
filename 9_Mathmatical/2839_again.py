import sys
input = sys.stdin.readline

N = int(input().strip())

# rest3 = N // 3 # 6
# rest5 = N // 5 # 3
# answers = []


# if N == 3 * rest3:
#     answers.append(rest3)
# if N == 5 * rest5:
#     answers.append(rest5)

# for i in range(1, rest3 + 1):
#     total = 3 * i
#     for j in range(1, rest5 + 1):
#         total += 5 * j
#         if total == N:
#             answers.append(i + j)
#         else:
#             total = 3 * i # 초기화 필요

# if answers:
#     print(min(answers))
# else:
#     print(-1)

count = 0
while N >= 0:
    if N % 5 == 0:
        count += N // 5
        print(count)
        break
    
    N -= 3
    count += 1
    
if N < 0:
    print(-1)