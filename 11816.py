import sys
input = sys.stdin.readline

X = input().strip()

if '0x' == X[:2]:
    print(int(X, 16))
elif '0' == X[0]:
    print(int(X, 8))
else:
    print(X)
