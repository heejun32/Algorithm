def solution(s):
    if len(s) == 4 or len(s) == 6:
        for digit in s:
            if not digit.isdigit():
                return False
        return True
    else:
        return False
