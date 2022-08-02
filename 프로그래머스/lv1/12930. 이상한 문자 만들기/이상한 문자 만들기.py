def solution(s):
    answer = []
    for word in s.split(' '):
        temp = ""
        for i in range(len(word)):
            # 홀 짝 판단
            if i % 2 == 0:
                temp += word[i].upper()
            else:
                temp += word[i].lower()
        answer.append(temp)
                
    return ' '.join(answer)