import sys


def dfs(hp, previous_people, previous_damage):
    global answer
    answer = max(answer, previous_people)
    
    for i in range(N):
        if not visited[i] and hp - A[i] - previous_damage >= 0:
            damage = A[i] + previous_damage
            visited[i] = True 
            dfs(hp - damage, previous_people + P[i], damage)
            visited[i] = False
    return
    

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
P = list(map(int, sys.stdin.readline().split()))
visited = [False] * N
answer = -1

# 백 트랙킹
dfs(K, 0, 0)
if answer < 0:
    print(0)
else:
    print(answer)
