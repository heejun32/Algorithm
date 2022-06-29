import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
end = 666

while True:
    if "666" in str(end):
        cnt += 1
    if cnt == N:
        print(end)
        break
    end += 1
