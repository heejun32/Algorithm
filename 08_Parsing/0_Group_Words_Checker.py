def solution():
    N = int(input())
    answer = N
    for _ in range(N):
        word = input()

        for i in range(len(word) - 1):
            if word[i] == word[i+1]:
                continue
            elif word[i] in word[i+1:]:
                answer -= 1
                break

    return answer

print(solution())