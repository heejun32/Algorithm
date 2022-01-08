def d(n):
    result = n
    n = str(n)

    for digit in n:
        result += int(digit)

    return result

def solution():
    i = 1
    self_numbers = []

    while (i < 10001):
        self_numbers.append(d(i))
        i += 1

    j = 1
    while (j < 10001):
        if j not in self_numbers:
            print(j)
        j += 1

solution()