N = input()
left = N[:len(N) // 2]
right = N[len(N) // 2:]
left_sum = 0
right_sum = 0

for i in range(len(N) // 2):
    left_sum += int(left[i])
    right_sum += int(right[i])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")