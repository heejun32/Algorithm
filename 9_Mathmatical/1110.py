N = input()
answer = N
new_number = -1
count = 0

while(answer != str(new_number)):
    digit_sum = 0
    for digit in N:
        digit_sum += int(digit)

    new_number = int(N[-1] + str(digit_sum)[-1])
    N = str(new_number)
    count += 1

print(count)