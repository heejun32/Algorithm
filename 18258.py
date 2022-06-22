from collections import deque
import sys
input = sys.stdin.readline

def push(queue, X):
    queue.append(X)

def pop(queue):
    if len(queue) > 0:
        print(queue.popleft())
    else:
        print(-1)

def size(queue):
    print(len(queue))

def empty(queue):
    if (len(queue) == 0):
        print(1)
    else:
        print(0)

def front(queue):
    if (len(queue) > 0):
        print(queue[0])
    else:
        print(-1)

def back(queue):
    if (len(queue) > 0):
        print(queue[-1])
    else:
        print(-1)

N = int(input())
queue = deque()

for _ in range(N):
    orders = list(input().split())

    if orders[0] == "push":
        push(queue, orders[1])

    if orders[0] == "pop":
        pop(queue)

    if orders[0] == "size":
        size(queue)

    if orders[0] == "empty":
        empty(queue)

    if orders[0] == "front":
        front(queue)

    if orders[0] == "back":
        back(queue)