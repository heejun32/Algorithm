TEST_CASE = int(input())

def check_even(string):
    stack = []

    for char in string:
        if char == '(' or char == '{':
            stack.append(char)
        elif char == ')' or char == '}':
            if not stack:
                return 0
            elif char == ')' and stack.pop() != '(':
                return 0
            elif char == '}' and stack.pop() != '{':
                return 0
    if stack:
        return 0
    return 1

for test in range(1, TEST_CASE + 1):
    string = input()
    print(f"#{test} {check_even(string)}")

# 분기문의 명확학 조건을 이해해라!
