A, B, V = map(int, input().split())
#
#
# V <= A * day - (B * (day - 1))
#
# V <= A * day - (B * day - B)
#
# V - B <= (A - B) * day

day = (V - B) / (A - B)

if day > int(day):
    day = day + 1

print(int(day))