N, M = map(int, input().split())

if N > M:
    max = N
    min = M
else:
    max = M
    min = N

gcf = 0 # 최대 공약수
lcm = 0 # 최소 공배수

while(max > 0):
    if N % max == 0 and M % max == 0:
        gcf = max
        break
    max -= 1

i = 1
while True:
    if (min * i) % N == 0 and (min * i) % M == 0:
        lcm = min * i
        break
    i += 1

print(gcf)
print(lcm)