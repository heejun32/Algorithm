N = int(input())

def solution(N):
    queue = [i for i in range(1, N + 1)]
    answer = []

    while(len(queue) > 1):
        answer.append(queue.pop(0))
        queue.append(queue.pop(0))

    for i in answer:
        print(i, end=" ")
    print(queue[0])

solution(N)