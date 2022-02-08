T = int(input())

for _ in range(T):
    P = [0, 1, 1, 1, 2, 2]
    N = int(input())

    if N < 6:
        print(P[N])
    else:
        for i in range(6, N + 1):
            P.append(P[i-1] + P[i-5])
        print(P[N])