def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ranking = {1: 0, 2: 0, 3: 0}
    
    # 채점
    for idx, a in enumerate(answers):
        # supoja1
        if a == s1[idx % 5]:
            ranking[1] += 1
        
        # supoja2
        if a == s2[idx % 8]:
            ranking[2] += 1
        
        # supoja3
        if a == s3[idx % 10]:
            ranking[3] += 1
    
    # 최다 득점자 확인
    max_answer = max(ranking.values())
    for key, value in ranking.items():
        if value == max_answer:
            answer.append(key)
            
    # 정답 출력 조건
    answer.sort()
    return answer