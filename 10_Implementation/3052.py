rest = []
for i in range(10):
    number = int(input())
    rest.append(number % 42)

rest = set(rest)
print(len(rest))