word = input()

def solution(word):
    dict = {}
    word = word.lower()

    for alpha in word:
        if alpha in dict.keys():
            dict[alpha] += 1
        else:
            dict[alpha] = 1

    answer = max(dict.values())
    count = 0

    for value in dict.values():
        if answer == value:
            count += 1

    if count > 1:
        print('?')
    else:
        for key in dict.keys():
            if answer == dict[key]:
                print(key.upper())

solution(word)