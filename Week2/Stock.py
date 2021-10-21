def solution(prices):
    count = [0] * len(prices)
    answer = []

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                count[i] += 1
            else:
                count[i] += 1
                break

        answer.append(count[i])
    return answer