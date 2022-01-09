H, M = map(int, input().split())

if (M - 45 < 0):
    if H != 0:
        H = H - 1
    else:
        H = 23
    M = (60 - -1 * (M - 45))

else:
    M = M - 45

print(f"{H} {M}")