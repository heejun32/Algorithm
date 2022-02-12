def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : 3 * x, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer

print(solution([6, 10, 2]))

# 아스키 코드로 문자열 값들을 비교내 내림차순 정리! 아스키 값이 큰 문자열이 앞으로 올수록, 제일 높은 자리의 숫자가 커지는 것이기 때문에 내림차순임!
# '321' '3'이 있을때 아스키 코드 비교시 앞자리 3만 비교해서 우위를 판단할 수 없음. 그래서 문제 조건인 각 숫자는 3자리 이하다라는 것을 활용
# 임의로 '3'을 3자리로 늘려 '333' '321'을 비교해 3이 321보다 먼저 정렬되게 작성한것임!
# 마지막 int()는 0 리스트 받을시의 예외처리임!