T = int(input())

def sol(T):
    for _ in range(T):
        R, S = input().split()
        repeat_alpha = ""

        for alpha in S:
            repeat_alpha += alpha * int(R)

        print(repeat_alpha)

sol(T)