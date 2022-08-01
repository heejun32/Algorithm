def solution(s):
    # 단어 나누기
    s = s.split(' ')
    # 소문자 변환
    for i in range(len(s)):
        # 첫글자 대문자 변환
        s[i] = s[i].capitalize()

    return ' '.join(s)
