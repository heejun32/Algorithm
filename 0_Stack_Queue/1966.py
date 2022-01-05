import sys
input = sys.stdin.readline

N = int(input())
count = 0

for _ in range(N):
    count = 0
    documents_info = list(map(int, input().split()))
    documents = [0] * documents_info[0]

    for i in range(documents_info[0]):
        documents[i] = i

    answer = documents_info[1]
    importance = list(map(int, input().split()))

    while (len(importance) > 0):
        if importance[0] >= max(importance):
            importance.pop(0)
            index = documents.pop(0)
            count += 1
            if answer == index:
                print(count)
        else:
            importance.append(importance.pop(0))
            documents.append(documents.pop(0))