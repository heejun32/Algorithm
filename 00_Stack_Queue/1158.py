'''
1 2 3 4 5 6 7   7       3
1 2 [] 4 5 6 7  6       6
1 2 [] 4 5 [] 7 5       2
1 [] [] 4 5 [] 7 4      7
1 [] [] 4 5 [] [] 3     5
1 [] [] 4 [] [] [] 2    4
1 [] [] [] [] [] [] 1   1
'''

# from collections import deque
# import sys
# input = sys.stdin.readline
#
# arr = deque()
# answer = []
# N, K = list(map(int, input().split()))
#
# for i in range(1, N + 1):
#     arr.append(i)
#
# while(len(arr) > 0):
#     arr.rotate(-(K-1))
#     answer.append(arr.popleft())
#
# print('<' + ", ".join(map(str, answer)) + '>')

import sys
input = sys.stdin.readline

arr = []
answer = []
N, K = list(map(int, input().split()))

for i in range(1, N + 1):
     arr.append(i)

index = 0
for _ in range(N):
    index = (index + K - 1) % len(arr)
    answer.append(arr.pop(index))

print('<' + ", ".join(map(str, answer)) + '>')