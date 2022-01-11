from collections import deque
import sys
input = sys.stdin.readline

def push_front(queue, X):
    return queue.appendleft(X)

def push_back(queue, X):
    return queue.append(X)

def pop_front(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.popleft())

def pop_back(queue):
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.pop())

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
queue = deque()

for _ in range(N):
    orders = list(input().split())

    if orders[0] == "push_front":
        push_front(queue, int(orders[1]))

    if orders[0] == "push_back":
        push_back(queue, int(orders[1]))

    if orders[0] == "pop_front":
        pop_front(queue)

    if orders[0] == "pop_back":
        pop_back(queue)

    if orders[0] == "size":
        size(queue)

    if orders[0] == "empty":
        empty(queue)

    if orders[0] == "front":
        front(queue)

    if orders[0] == "back":
        back(queue)