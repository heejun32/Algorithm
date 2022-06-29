import sys
input = sys.stdin.readline
M = int(input())

def add(S, x):
    if not x in S:
        S.append(x)

def remove(S, x):
    if x in S:
        S.remove(x)

def check(S, x):
    if x in S:
        print(1)
    else:
        print(0)

def toggle(S, x):
    if x in S:
        S.remove(x)
    else:
        S.append(x)

def all(S):
    S = [i for i in range(1, 21)]
    return S

def empty(S):
    S = []
    return S

S = []
for _ in range(M):
    operation = list(input().split())
    order = operation[0]

    if len(operation) > 1:
        value = int(operation[-1])

    if order == 'add':
        add(S, value)
    if order == 'remove':
        remove(S, value)
    if order == 'check':
        check(S, value)
    if order == 'toggle':
        toggle(S, value)
    if order == 'all':
        S = all(S)
    if order == 'empty':
        S = empty(S)
