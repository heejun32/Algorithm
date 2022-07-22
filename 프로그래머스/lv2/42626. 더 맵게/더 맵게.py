import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    count = 0
    
    while scoville[0] < K:
        if len(scoville) >= 2:
            new_food = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)
            heapq.heappush(scoville, new_food)
            count += 1
        else:
            break
    if scoville[0] < K:
        return - 1
    
    return count