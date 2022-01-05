import sys
input = sys.stdin.readline

def push(queue, x):
    queue.append(x)
    return queue

def pop(queue):
    if len(queue) == 0:
        print(-1)
        return queue
    else:
        print(queue.pop(0))
        return queue

def size(queue):
    print(len(queue))

def empty(queue):
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])

N = int(input())
queue = []

for _ in range(N):
    order = list(input().split())

    if (order[0] == "push"):
        push(queue, order[1])

    if (order[0] == "pop"):
        queue = pop(queue)

    if (order[0] == "front"):
        front(queue)

    if (order[0] == "back"):
        back(queue)

    if (order[0] == "size"):
        size(queue)

    if (order[0] == "empty"):
        empty(queue)