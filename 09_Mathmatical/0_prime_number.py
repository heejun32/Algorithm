def solution():
    answer = int(input())
    numbers = map(int, list(input().split()))
    # 소수는 1과 자기자신만 약수로 가지눈 숫자
    # 그럼 자기자신이 아닌 숫자 중에 하나라도 약수로 가지게 되면 소수가 아님!

    for number in numbers:
        if number == 1:
            answer -= 1
            continue
        if number == 2:
            continue

        for num in range(2, number):
            if  number % num == 0:
                answer -= 1
                break

    return answer

print(solution())