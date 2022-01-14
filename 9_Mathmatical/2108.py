N = int(input())
numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)

numbers.sort()
mean = round(sum(numbers) / len(numbers))
middle = numbers[len(numbers) // 2]
scope = numbers[-1] - numbers[0]

mfreq = 0
my_dict = {}
for i in numbers:
    if i not in my_dict.keys():
        my_dict[i] = 1
    else:
        my_dict[i] += 1

frequences = list(my_dict.values())
print(frequences)
mfreq2 = frequences.sort()[-2]
for key, value in my_dict:
    if value == mfreq2:
        mfreq = key
        break

print(mean)
print(middle)
print(mfreq)
print(scope)