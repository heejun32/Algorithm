from itertools import combinations

N, M = map(int, input().split())
NUM_LIST = list(map(int, input().split()))

def solution(N, M, NUM_LIST):
    answer = 0

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                sum = NUM_LIST[i] + NUM_LIST[j] + NUM_LIST[k]
                if sum > M:
                    continue
                else:
                    if answer < sum:
                        answer = sum

    return answer

def solution2(N, M, NUM_LIST):
    answer = 0

    for cards in combinations(NUM_LIST, 3):
        temp_sum = sum(cards)

        if answer < temp_sum <= M:
            answer = temp_sum

    return answer

# print(solution(N, M, NUM_LIST))
print(solution2(N, M, NUM_LIST))