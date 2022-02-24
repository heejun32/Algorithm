import sys
import heapq
input = sys.stdin.readline

# v: 선호도, c: 도수
N, M, K = map(int, input().split())
beers = []
for _ in range(K):
    v, c = map(int, input().split())
    beers.append([v, c])

# 도수가 낮은 순으로 정렬
beers.sort(key=lambda x:(x[1]))
preference = 0
heap = []

for beer in beers:
    preference += beer[0]
    heapq.heappush(heap, beer[0])
    
    # N병 만큼 마시면
    if len(heap) == N:
        if preference >= M:
            answer = beer[1] # 도수가 낮은 순으로 정렬 되어 있기에
            break
        else:
            # 선호도를 못채우면
            preference -= heapq.heappop(heap) # 선호도가 제일 낮은 맥주를 뺀다


if len(heap) != N:
    print(-1)
else:
    print(answer)