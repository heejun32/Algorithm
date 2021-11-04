def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer



print(solution([6, 10, 2]))

### 다시 공부하기!
https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%88%98-%EC%A0%95%EB%A0%AC