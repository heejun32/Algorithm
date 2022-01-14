import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)

numbers.sort()
mean = round(sum(numbers) / len(numbers))
middle = numbers[len(numbers) // 2]
scope = abs(numbers[-1] - numbers[0])
mfreq = 0

from collections import Counter

# f_dict = {}
# for i in numbers:
#     if i in f_dict.keys():
#         f_dict[i] += 1
#     else:
#         f_dict[i] = 1
#
# f_list = []
# for key, value in f_dict.items():
#     f_list.append([key, value])
# f_list.sort(key=lambda x: (-x[1], x[0]))

f_list = Counter(numbers).most_common(2)
print(f_list)
if len(f_list) > 1:
        if f_list[0][1] != f_list[1][1]:
            mfreq = f_list[0][0]
        else:
            mfreq = f_list[1][0]
else:
    mfreq = f_list[0][0]

print(mean)
print(middle)
print(mfreq)
print(scope)