def DFS(begin, target, words, visit):
    stack = [begin]
    lengh = 0

    while (stack):
        print(stack)
        print(visit)
        temp = stack.pop()

        if temp == target:
            return lengh

        for idx1 in range(len(words)):
            if visit[idx1] == True:
                continue

            cnt = 0
            for idx2 in range(len(words[idx1])):
                if temp[idx2] != words[idx1][idx2]:
                    cnt += 1
            if cnt == 1:
                visit[idx1] = True
                if words[idx1] == target:       #이 예외처리가 핵심...
                    stack.append(words[idx1])
                    break
                stack.append(words[idx1])
        lengh += 1
    return 0

def solution(begin, target, words):
    if target not in words:
        return 0

    if begin == target:
        return 1

    visit = [False] * len(words)
    answer = DFS(begin, target, words, visit)
    return answer

print("결과: ", solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
print()
print("결과: ", solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
print()
print("결과: ", solution('hit', 'cog', ['cog', 'log', 'lot', 'dog', 'dot', 'hot']))


'''
총평: 최단 경로를 찾기에 DFS라고 할 수 있음. 최단 경로(단어)로 가기 위해 방문하지 않은 모든 단어를 확인하고 가장 차이가 적은 단어로 옮기기.
예제에서는 작동 안해도 테스트 케이스에서는 작동되는 아주 이상한 경우가 존재. 항상 이 둘을 교차 검증할 것! / 맞았다고 넘어가지 말고 이해하고 넘어가기!
'''