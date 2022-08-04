def solution(numbers, target):
    result = [0]

    for num in numbers:
        temp = []
        for r in result:
            temp.append(r + num)
            temp.append(r - num)
        result = temp

    return result.count(target)
