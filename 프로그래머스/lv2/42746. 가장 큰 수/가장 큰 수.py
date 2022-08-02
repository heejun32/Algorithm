def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 9, reverse=True)
    
    return str(int(''.join(numbers)))