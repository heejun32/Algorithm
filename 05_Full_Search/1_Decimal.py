from itertools import permutations
import math


def is_prime(n):
    sqrt_num = int(math.sqrt(n))

    if n < 2:
        return False

    for i in range(2, sqrt_num + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    num_list = [number for number in numbers]
    combination = []
    sort_combination = []
    answer = 0

    for i in range(1, len(numbers) + 1):
        combination += list(permutations(num_list, i))

    for comb in combination:
        sort_combination.append(int(("").join(comb)))

    sort_combination = set(sort_combination)

    for comb in sort_combination:
        if is_prime(comb) == True:
            answer += 1

    return answer


print(solution("17"))
print(solution("011"))