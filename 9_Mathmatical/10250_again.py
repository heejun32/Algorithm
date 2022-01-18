T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    room =  N // H + 1

    if floor == 0:
        floor = H
        room -= 1
    print(floor * 100 + room)

    # 6 12 = 72 / 이 경우 6의 배수일때마다 호수의 w가 1증가, 그게 아니라면 hf를 1씩 증가