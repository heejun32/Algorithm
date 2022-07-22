def solution(numbers):
    answer = set()
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            summation = numbers[i] + numbers[j]
            if summation not in answer:
                answer.add(summation)
    return sorted(answer)