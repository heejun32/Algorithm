def solution(answers):
    answer = []
    supoja1 = [1, 2, 3, 4, 5]
    supoja2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    supojas_ans_cnt = [0] * 3

    for i in range(len(answers)):
        if answers[i] == supoja1[i % len(supoja1)]:
            supojas_ans_cnt[0] += 1
        if answers[i] == supoja2[i % len(supoja2)]:
            supojas_ans_cnt[1] += 1
        if answers[i] == supoja3[i % len(supoja3)]:
            supojas_ans_cnt[2] += 1

    max_ans_cnt = max(supojas_ans_cnt)
    for i in range(len(supojas_ans_cnt)):
        if max_ans_cnt == supojas_ans_cnt[i]:
            answer.append(i + 1)
    return answer