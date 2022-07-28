def divisor(num):
    # 예외처리
    if num == 1:
        return 0
    
    # 시작: 모든 수는 제일 작은 약수로 1을 가진다.
    for div in range(2, int(num ** 0.5) + 1):
        if num % div == 0 and num / div <= 10 ** 7:
            # 제일 큰 약수를 찾아야 하기에, 맞은편 약수를 찾으면 반대편 약수를 저장해준다!
            return num / div
    return 1

def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        answer.append(divisor(i))
    return answer
