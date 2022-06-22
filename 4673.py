def d(n):
    result = n

    for digit in str(n):
        result += int(digit)

    return result

def solution():
    i = 1
    self_numbers = []

    for i in range(1, 10001):
        self_numbers.append(d(i))

    for j in range(1, 10001):
        if j not in self_numbers:
            print(j)
        j += 1

solution()