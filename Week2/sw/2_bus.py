lines = int(input())

for line in range(lines):
    K, N, M = map(int, input().split())
    charges_list = list(map(int, input().split()))

    stops = [0] * (N + 1)
    for i in range(len(charges_list)):
        stops[charges_list[i]] = 1 # 충전소 위치 정류장에 표시

    bus_start = K
    count = 0

    while bus_start < N:
        if stops[bus_start] == 1:
            stops[bus_start] = 2 # 한번 도착한 충전소는 다르게 표시
            bus_start = bus_start + K
            count = count + 1
        elif stops[bus_start] == 2 or bus_start ==0:
            count = 0
            break
        else:
            bus_start -= 1
            continue

    if (count == 0):
        print("#{} {}".format(line + 1, count))
    else:
        print("#{} {}".format(line + 1, count))

