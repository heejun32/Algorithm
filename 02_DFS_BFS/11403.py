import sys
input = sys.stdin.readline

def DFS(row):
    stack = []


N = int(input())
G = []
V = [False for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    G.append(row)

for row in G:
    DFS(row)
