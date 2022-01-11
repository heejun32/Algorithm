N = int(input())
words = []

for i in range(N):
    word = input()
    if word in words:
        continue
    else:
        words.append(word)
# Tim sort를 공부한 뒤 sorted를 사용할 것! 병합정렬 공부 뒤에 이 문제는 다시 풀기
for i in range(len(words) - 1):
    for j in range(i + 1, len(words)):
        if len(words[i]) > len(words[j]):
            temp = words[i]
            words[i] = words[j]
            words[j] = temp

        if len(words[i]) == len(words[j]) and words[i] > words[j]:
            temp = words[i]
            words[i] = words[j]
            words[j] = temp

for word in words:
    print(word)
