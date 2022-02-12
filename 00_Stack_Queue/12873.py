from collections import deque

N = int(input())

def solution(N):
    people = deque()
    for i in range(1, N + 1):
        people.append(i)

    for stage in range(1, N):
        remove = stage ** 3
        people.rotate(-(remove - 1))
        people.popleft()

    print(people[0])

solution(N)
