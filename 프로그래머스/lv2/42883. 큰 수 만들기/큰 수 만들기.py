def solution(number: str, k: int) -> str:
    stack = []
    
    for num in number:
        while stack and stack[-1] < num and k:
            stack.pop()
            k -= 1
        stack.append(num)

    return "".join(stack[:len(stack) - k])