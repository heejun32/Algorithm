def solution(citations):
    answer = 0
    # 1. 내림차순 정렬
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] >= i + 1:  # 논문의 번호는 1번부터 시작 그래서 인용횟수와 i+1(번호) 로 비교
            answer = i + 1

    return answer
# 프로그래머스 문제 해석이 이상해서 직접 h-index 내용 조회
# 사이트 주소: https://hanyang-kr.libguides.com/c.php?g=717952 백남 학술정보원
# 학술정보원에서 h-index 구하는 법에 대해 자세히 설명되어 있어 해결함