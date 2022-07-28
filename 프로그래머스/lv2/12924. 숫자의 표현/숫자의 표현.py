def solution(n):
    answer = 0
    numbers = [i for i in range(1, n + 1)]
    left = 0
    right = 0
    while right <= n:
        if sum(numbers[left: right]) < n:
            right += 1
        if sum(numbers[left: right]) == n:
            answer += 1
            right += 1
        if sum(numbers[left: right]) > n:
            left += 1
    return answer