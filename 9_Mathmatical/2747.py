N = int(input())

def fibonacci(n):
    answer = [0, 1]
    while n > 1:
        answer.append(answer[-1] + answer[-2])
        n -= 1

    return answer[-1]

print(fibonacci(N))